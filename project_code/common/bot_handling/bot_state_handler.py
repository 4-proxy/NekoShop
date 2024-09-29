# -*- coding: utf-8 -*-

"""
The `bot_state_handler` module manages the state of the Telegram bot.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    "on_startup",
    "on_shutdown",
    "logger"
]

__author__ = "4-proxy"
__version__ = "1.1.2"

import aiogram

import logging

from common.workflow_intermediary import WorkflowIntermediary


logger: logging.Logger = logging.getLogger(name=__name__)


# -----------------------------------------------------------------------------
async def on_startup() -> None:
    """Handle actions to perform when the bot starts.

    Sends a notification message to the owner's chat and logs the startup event.
    """
    bot: aiogram.Bot = WorkflowIntermediary.current_bot
    chat_id: str = WorkflowIntermediary.owner_chat_id
    startup_message = "I'am wake up!"
    startup_log_message = "Bot is online!"

    logger.info(msg=startup_log_message)

    await bot.send_message(chat_id=chat_id,
                           text=startup_message)


# -----------------------------------------------------------------------------
async def on_shutdown() -> None:
    """Handle actions to perform when the bot stops.

    Sends a notification message to the owner's chat and logs the shutdown event.
    """
    bot: aiogram.Bot = WorkflowIntermediary.current_bot
    chat_id: str = WorkflowIntermediary.owner_chat_id
    shutdown_message = "I'am go to sleep!"
    shutdown_log_message = "Bot is shutdown!"

    logger.info(msg=shutdown_log_message)

    await bot.send_message(chat_id=chat_id,
                           text=shutdown_message)
