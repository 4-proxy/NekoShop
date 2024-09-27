# -*- coding: utf-8 -*-

"""
The `bot_state_handler` module is used to handle the state of the Telegram bot.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    "on_startup",
    "on_shutdown",
    "logger"
]

__author__ = "4-proxy"
__version__ = "1.1.0"

import aiogram

import logging

from ..workflow_intermediary import WorkflowIntermediary


logger: logging.Logger = logging.getLogger(name=__name__)


# -----------------------------------------------------------------------------
async def on_startup() -> None:
    """on_startup called when the bot is started.

    Sends a message to the owner chat.
    """
    bot: aiogram.Bot = WorkflowIntermediary.current_bot
    chat_id: str = WorkflowIntermediary.owner_chat_id
    message_text = "I'am wake up!"

    logger.info(msg="Bot is online!")

    await bot.send_message(chat_id=chat_id,
                           text=message_text)


# -----------------------------------------------------------------------------
async def on_shutdown() -> None:
    """on_shutdown called when the bot is stopped.

    Sends a message to the owner chat.
    """
    bot: aiogram.Bot = WorkflowIntermediary.current_bot
    chat_id: str = WorkflowIntermediary.owner_chat_id
    message_text = "I'am go to sleep!"

    logger.info(msg="Bot is shutdown!")

    await bot.send_message(chat_id=chat_id,
                           text=message_text)
