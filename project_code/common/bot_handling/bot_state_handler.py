# -*- coding: utf-8 -*-

"""
description

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = ["on_startup", "on_shutdown"]

__author__ = "4-proxy"
__version__ = "0.1.0"

import aiogram

from ..workflow_intermediary import WorkflowIntermediary


# -----------------------------------------------------------------------------
async def on_startup() -> None:
    bot: aiogram.Bot = WorkflowIntermediary.current_bot
    chat_id: str = WorkflowIntermediary.owner_chat_id

    await bot.send_message(chat_id=chat_id, text="I'am wake up!")


# -----------------------------------------------------------------------------
async def on_shutdown() -> None:
    bot: aiogram.Bot = WorkflowIntermediary.current_bot
    chat_id: str = WorkflowIntermediary.owner_chat_id

    await bot.send_message(chat_id=chat_id, text="I'am go to sleep!")
