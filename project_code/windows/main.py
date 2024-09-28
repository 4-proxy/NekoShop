# -*- coding: utf-8 -*-

"""
This script is used to launch the Telegram bot and all relevant components.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__author__ = "4-proxy"
__version__ = "0.5.0"

import aiogram

import os

from common.external_handling import logger_handler
from common.bot_handling import bot_handler
from common.bot_handling import bot_state_handler
from common.workflow_intermediary import WorkflowIntermediary
from common.external_handling.bot_config_handler import BotConfigDTO

from typing import NoReturn
from common.external_handling.json_handler import ContentJSON


FILEPATH_TO_PROJECT_CONFIG: str = os.path.join(
    "windows", "project_config.json"
)


# -----------------------------------------------------------------------------
async def configure_BotConfig() -> BotConfigDTO:
    from common.external_handling import json_handler

    project_config: ContentJSON = json_handler.get_content_from_json(
        filepath=FILEPATH_TO_PROJECT_CONFIG
    )

    bot_config = BotConfigDTO(
        api_token=project_config["Bot"]["API_TOKEN"],
        owner_chat_id=project_config["Bot"]["OWNER_CHAT_ID"],
        debug=project_config["Bot"]["DEBUG"]
    )

    return bot_config


# -----------------------------------------------------------------------------
async def configure_WorkflowIntermediary(bot_config: BotConfigDTO) -> None:
    api_token: str = bot_config.api_token
    owner_chat_id: str = bot_config.owner_chat_id

    telegram_bot: aiogram.Bot = await bot_handler.create_bot(api_token=api_token)

    WorkflowIntermediary.current_bot = telegram_bot
    WorkflowIntermediary.owner_chat_id = owner_chat_id


# -----------------------------------------------------------------------------
async def main() -> NoReturn:
    bot_config: BotConfigDTO = await configure_BotConfig()

    await configure_WorkflowIntermediary(bot_config=bot_config)

    telegram_bot: aiogram.Bot = WorkflowIntermediary.current_bot
    telegram_dispatcher: aiogram.Dispatcher = await bot_handler.create_dispatcher()

    telegram_dispatcher.startup.register(bot_state_handler.on_startup)
    telegram_dispatcher.shutdown.register(bot_state_handler.on_shutdown)

    await bot_handler.run_bot(bot=telegram_bot,
                              dispatcher=telegram_dispatcher)


if __name__ == "__main__":
    import asyncio

    try:
        asyncio.run(main=main())

    except KeyboardInterrupt:
        print("Bot is shutdown, manually!")
