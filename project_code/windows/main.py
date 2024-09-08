# -*- coding: utf-8 -*-

"""
description

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = []

__author__ = "4-proxy"
__version__ = "0.1.0"

from ..common.bot_handling.bot_handler import *
from ..common.bot_handling.bot_state_handler import *
from ..common.workflow_intermediary import WorkflowIntermediary

from typing import NoReturn


# -----------------------------------------------------------------------------
async def configure_WorkflowIntermediary() -> None:
    from .config import API_TOKEN, CHAT_ID

    WorkflowIntermediary.current_bot = await create_bot(api_token=API_TOKEN)
    WorkflowIntermediary.owner_chat_id = CHAT_ID


# -----------------------------------------------------------------------------
async def main() -> NoReturn:
    await configure_WorkflowIntermediary()

    telegram_bot = WorkflowIntermediary.current_bot
    telegram_dispatcher = await create_dispatcher()

    telegram_dispatcher.startup.register(callback=on_startup)
    telegram_dispatcher.shutdown.register(callback=on_shutdown)

    await run_bot(bot=telegram_bot,
                  dispatcher=telegram_dispatcher)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main=main())
