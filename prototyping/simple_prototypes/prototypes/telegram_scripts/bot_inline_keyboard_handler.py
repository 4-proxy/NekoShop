# -*- coding: utf-8 -*-

"""
The bot_inline_keyboard_handler module is used to demonstrate how the `inline` keyboard and `callback_query` functionality works.
functionality of `inline` keyboard and `callback_query`.
(Direct use of this module in the development of the final product is not provided).


Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = ["router", "test_status", "keyboard_builder"]

__author__ = "4-proxy"
__version__ = "1.0.1"

from aiogram import Router
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, CallbackQuery


router = Router(name=__name__)
test_status: list[str] = []

# Keyboard
keyboard_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
keyboard_button: InlineKeyboardButton = InlineKeyboardButton(
    text="Click me!", callback_data="Button is clicked!"
)
keyboard_builder.add(keyboard_button)


# CallbackQuery
@router.callback_query()
async def callback_click_me(query: CallbackQuery) -> None:
    if query.data == "Button is clicked!":
        test_status.append("OK")

    await query.answer(text="Callback is accepted!")
