# -*- coding: utf-8 -*-

"""
description

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = []

__author__ = "4-proxy"
__version__ = "0.2.0"

import aiogram

import os

from ..common.bot_handling.bot_handler import *
from ..common.bot_handling.bot_state_handler import *
from ..common.workflow_intermediary import WorkflowIntermediary
from ..common.external_handling.bot_config_handler import BotConfig

from typing import NoReturn
from project_code.common.external_handling.json_handler import ContentJSON


FILEPATH_TO_PROJECT_CONFIG: str = os.path.join(
    "project_code", "windows", "project_config.json"
)


# -----------------------------------------------------------------------------
async def configure_BotConfig() -> None:
    from ..common.external_handling import json_handler

    config_content: ContentJSON = json_handler.get_content_from_json(
        filepath=FILEPATH_TO_PROJECT_CONFIG
    )

    BotConfig.API_TOKEN = config_content["Bot"]["API_TOKEN"]
    BotConfig.OWNER_CHAT_ID = config_content["Bot"]["OWNER_CHAT_ID"]
    BotConfig.DEBUG = config_content["Bot"]["DEBUG"]


# -----------------------------------------------------------------------------
async def configure_WorkflowIntermediary() -> None:
    api_token: str = BotConfig.API_TOKEN
    owner_chat_id: str = BotConfig.OWNER_CHAT_ID

    WorkflowIntermediary.current_bot = await create_bot(api_token=api_token)
    WorkflowIntermediary.owner_chat_id = owner_chat_id


# -----------------------------------------------------------------------------
async def main() -> NoReturn:
    await configure_BotConfig()
    await configure_WorkflowIntermediary()

    telegram_bot: aiogram.Bot = WorkflowIntermediary.current_bot
    telegram_dispatcher: aiogram.Dispatcher = await create_dispatcher()

    telegram_dispatcher.startup.register(callback=on_startup)
    telegram_dispatcher.shutdown.register(callback=on_shutdown)

    await run_bot(bot=telegram_bot,
                  dispatcher=telegram_dispatcher)


if __name__ == "__main__":
    import asyncio

    try:
        asyncio.run(main=main())

    except KeyboardInterrupt:
        print("Bot is shutdown, manually!")

    except Exception:
        print("Bot is shutdown, unknown reason!")
