# -*- coding: utf-8 -*-

"""
The bot_handler module is used for processing, including customization of required components,
to run the telegram bot.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = ["create_dispatcher", "configure_bot", "run_bot"]

__author__ = "4-proxy"
__version__ = "1.0.1"

from aiogram import Dispatcher, Bot

from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from typing import Any


# ----------------------------------------------------------------------------
async def create_dispatcher(**kwargs: Any) -> Dispatcher:
    """create_dispatcher creates an instance of aiogram.Dispatcher.

    The function is used to create a dispatcher,
    which will be used to run the telegram bot.

    Returns:
        Dispatcher: A customized instance of Dispatcher.
    """
    telegram_dispatcher: Dispatcher = Dispatcher(**kwargs)

    return telegram_dispatcher


# ----------------------------------------------------------------------------
async def configure_bot(
    bot_token: str,
    default_param: DefaultBotProperties = DefaultBotProperties(
        parse_mode=ParseMode.HTML
    ),
) -> Bot:
    """configure_bot creates an instance of aiogram.Bot.

    The function is used to configure and create an instance of telegram bot,
    which will be passed to the dispatcher for launching.

    *If the bot token is not authorized in telegram, the function will not raise an exception.

    Args:
        bot_token (str): Bot token.
        default_param (DefaultBotProperties, optional): Key parameters for bot initialization.

    Returns:
        Bot: The customized bot instance.
    """
    bot = Bot(token=bot_token, default=default_param)

    return bot


# ----------------------------------------------------------------------------
async def run_bot(bot: Bot, dispatcher: Dispatcher) -> None:
    """run_bot launches a telegram bot online.

    The function is used to initiate the launch of a telegram bot,
    using the dispatcher and bot instance.

    Args:
        bot (Bot): A customized instance of aiogram.Bot.
        dispatcher (Dispatcher): A customized instance of aiogram.Dispatcher.
    """
    await dispatcher.start_polling(bot)  # type: ignore
