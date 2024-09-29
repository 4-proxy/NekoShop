# -*- coding: utf-8 -*-

"""
The `bot_handler` module is responsible for processing
and configuring the necessary components to run the Telegram bot.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    "create_dispatcher",
    "create_bot",
    "run_bot"
]

__author__ = "4-proxy"
__version__ = "1.0.3"

from aiogram import Dispatcher, Bot

from aiogram.enums.parse_mode import ParseMode
from typing import Any


# -----------------------------------------------------------------------------
async def create_dispatcher(**kwargs: Any) -> Dispatcher:
    """Create a dispatcher object to handle Telegram bot updates.

    This function accepts arbitrary keyword arguments that are passed to the
    `aiogram.Dispatcher` constructor.

    Args:
        **kwargs (Any): Arbitrary keyword arguments for dispatcher configuration.

    Returns:
        Dispatcher: Configured instance of `aiogram.Dispatcher`.
    """
    dispatcher = Dispatcher(**kwargs)

    return dispatcher


# ----------------------------------------------------------------------------
async def create_bot(api_token: str,
                     parse_mode: ParseMode = ParseMode.HTML) -> Bot:
    """Create a bot object to interact with Telegram.

    This function initializes a bot instance using the provided API token and
    sets the default message parsing mode.

    Args:
        api_token (str): Bot API token received from @BotFather [https://t.me/BotFather].
        parse_mode (ParseMode): Message parsing mode. Defaults to `ParseMode.HTML`.

    Returns:
        Bot: Configured instance of `aiogram.Bot`.

    Raises:
        TokenValidationError: When token has invalid format this exception will be raised.
    """
    bot = Bot(token=api_token)

    bot.default.parse_mode = parse_mode

    return bot


# ----------------------------------------------------------------------------
async def run_bot(*, bot: Bot,
                  dispatcher: Dispatcher) -> None:
    """Run the bot and start listening for updates.

    This function initiates polling for updates using the provided bot and dispatcher instances.

    Args:
        bot (Bot): Configured instance of `aiogram.Bot`.
        dispatcher (Dispatcher): Configured instance of `aiogram.Dispatcher`.
    """
    await dispatcher.start_polling(bot)  # type: ignore
