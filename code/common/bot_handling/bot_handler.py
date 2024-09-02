# -*- coding: utf-8 -*-

"""
description

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = ["create_dispatcher", "create_bot", "run_bot"]

__author__ = "4-proxy"
__version__ = "0.2.0"

from aiogram import Dispatcher, Bot

from aiogram.enums.parse_mode import ParseMode
from typing import Any


# -----------------------------------------------------------------------------
async def create_dispatcher(**kwargs: Any) -> Dispatcher:
    dispatcher = Dispatcher(**kwargs)

    return dispatcher

# ----------------------------------------------------------------------------


async def create_bot(api_token: str,
                     parse_mode: ParseMode = ParseMode.HTML) -> Bot:
    bot = Bot(token=api_token)

    bot.default.parse_mode = parse_mode

    return bot

# ----------------------------------------------------------------------------


async def run_bot() -> None:
    pass
