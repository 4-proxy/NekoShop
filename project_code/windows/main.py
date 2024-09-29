# -*- coding: utf-8 -*-

"""
This script launches a Telegram bot, configuring it with settings from a JSON file.
It initializes the bot and sets up necessary components for handling messages and commands.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__author__ = "4-proxy"
__version__ = "0.5.1"

import aiogram

import os

from common.external_handling import logger_handler
from common.bot_handling import bot_handler
from common.bot_handling import bot_state_handler
from common.workflow_intermediary import WorkflowIntermediary
from common.external_handling.bot_config_handler import BotConfigDTO

from typing import NoReturn
from common.external_handling.json_handler import ContentJSON


PROJECT_CONFIG_FILEPATH: str = os.path.join(
    "windows", "project_config.json"
)


# -----------------------------------------------------------------------------
async def configure_BotConfig() -> BotConfigDTO:
    """Load and configure the bot settings from a JSON configuration file.

    This function reads the project configuration from a specified JSON file,
    extracts the bot's API token, owner chat ID, and debug mode settings,
    and returns a `BotConfigDTO` object containing these values.

    Returns:
        BotConfigDTO: A data transfer object containing the bot's configuration settings.
    """
    from common.external_handling import json_handler

    project_config: ContentJSON = json_handler.parse_content_from_json(
        filepath=PROJECT_CONFIG_FILEPATH
    )

    bot_config = BotConfigDTO(
        api_token=project_config["Bot"]["API_TOKEN"],
        owner_chat_id=project_config["Bot"]["OWNER_CHAT_ID"],
        debug=project_config["Bot"]["DEBUG"]
    )

    return bot_config


# -----------------------------------------------------------------------------
async def configure_WorkflowIntermediary(bot_config: BotConfigDTO) -> None:
    """Set up the WorkflowIntermediary with the provided bot configuration.

    This function creates an instance of the Telegram bot using the API token
    from the provided bot configuration and assigns it to the `WorkflowIntermediary`.
    It also sets the owner chat ID for future reference.

    Args:
        bot_config (BotConfigDTO): The configuration object containing API token
                                    and owner chat ID.
    """
    api_token: str = bot_config.api_token
    owner_chat_id: str = bot_config.owner_chat_id

    bot_instance: aiogram.Bot = await bot_handler.create_bot(api_token=api_token)

    WorkflowIntermediary.current_bot = bot_instance
    WorkflowIntermediary.owner_chat_id = owner_chat_id


# -----------------------------------------------------------------------------
async def main() -> NoReturn:
    """Main entry point for launching the Telegram bot.

    This function orchestrates the configuration of the bot and its components,
    including setting up the dispatcher for handling incoming messages and events.

    It runs indefinitely until interrupted by a `KeyboardInterrupt`.

    Returns:
        NoReturn: This function does not return a value.
    """
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
