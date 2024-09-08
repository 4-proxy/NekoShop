# -*- coding: utf-8 -*-

"""
The `bot_handler` module is used for processing, including setting up the necessary components,
to run the Telegram bot.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = ["create_dispatcher", "create_bot", "run_bot"]

__author__ = "4-proxy"
__version__ = "1.0.1"

from aiogram import Dispatcher, Bot

from aiogram.enums.parse_mode import ParseMode
from typing import Any


# -----------------------------------------------------------------------------
async def create_dispatcher(**kwargs: Any) -> Dispatcher:
    """create_dispatcher create dispatcher object to handle Telegram bot updates.

    Accepts arbitrary key arguments that are passed to aiogram.Dispatcher constructor.

    Returns:
        Dispatcher: configured instance of aiogram.Dispatcher
    """
    dispatcher = Dispatcher(**kwargs)

    return dispatcher


# ----------------------------------------------------------------------------
async def create_bot(api_token: str,
                     parse_mode: ParseMode = ParseMode.HTML) -> Bot:
    """create_bot creates bot object to interact with Telegram.

    Args:
        api_token (str): bot API token received from @BotFather [https://t.me/BotFather].
        parse_mode (ParseMode): Message parsing mode. Defaults to ParseMode.HTML.

    Returns:
        Bot: configured instance of aiogram.Bot.
    """
    bot = Bot(token=api_token)

    bot.default.parse_mode = parse_mode

    return bot


# ----------------------------------------------------------------------------
async def run_bot(*, bot: Bot, dispatcher: Dispatcher) -> None:
    """run_bot runs the bot and starts listening for updates.

    Args:
        bot (Bot): configured instance of aiogram.Bot.
        dispatcher (Dispatcher): configured instance of aiogram.Dispatcher.
    """
    await dispatcher.start_polling(bot)  # type: ignore
