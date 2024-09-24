# -*- coding: utf-8 -*-

"""
This script is used to launch the Telegram bot and all relevant components.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__author__ = "4-proxy"
__version__ = "0.4.0"

import aiogram

import os

from common.external_handling import logger_handler
from common.bot_handling import bot_handler
from common.bot_handling import bot_state_handler
from common.workflow_intermediary import WorkflowIntermediary
from common.external_handling.bot_config_handler import BotConfig

from typing import NoReturn
from common.external_handling.json_handler import ContentJSON


FILEPATH_TO_PROJECT_CONFIG: str = os.path.join(
    "windows", "project_config.json"
)


# -----------------------------------------------------------------------------
async def configure_BotConfig() -> None:
    from common.external_handling import json_handler

    project_config: ContentJSON = json_handler.get_content_from_json(
        filepath=FILEPATH_TO_PROJECT_CONFIG
    )

    BotConfig.API_TOKEN = project_config["Bot"]["API_TOKEN"]
    BotConfig.OWNER_CHAT_ID = project_config["Bot"]["OWNER_CHAT_ID"]
    BotConfig.DEBUG = project_config["Bot"]["DEBUG"]


# -----------------------------------------------------------------------------
async def configure_WorkflowIntermediary() -> None:
    api_token: str = BotConfig.API_TOKEN
    owner_chat_id: str = BotConfig.OWNER_CHAT_ID

    WorkflowIntermediary.current_bot = await bot_handler.create_bot(api_token=api_token)
    WorkflowIntermediary.owner_chat_id = owner_chat_id


# -----------------------------------------------------------------------------
async def main() -> NoReturn:
    await configure_BotConfig()
    await configure_WorkflowIntermediary()

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

    except Exception as error:
        print(f"Bot is shutdown, unknown reason!\n{error}")
