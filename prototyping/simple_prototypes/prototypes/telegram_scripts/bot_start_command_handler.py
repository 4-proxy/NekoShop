# -*- coding: utf-8 -*-

"""
The bot_start_command_handler module is used to demonstrate the work of the
bot command handler.
(Direct use of this module in the development of the final product is not provided).

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = ["router", "test_status"]

__author__ = "4-proxy"
__version__ = "1.0.1"

from aiogram import Router

from aiogram.types import Message
from aiogram.filters import Command


router = Router(name=__name__)
test_status: list[str] = []


# -----------------------------------------------------------------------------
@router.message(Command("start", ignore_case=True))
async def cmd_start(msg: Message) -> None:
    test_status.append("OK")
