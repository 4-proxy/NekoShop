# -*- coding: utf-8 -*-

"""
The test_bot_state_handlers module is a set of unit tests,
for testing components of the bot_state_handlers module.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__author__ = "4-proxy"
__version__ = "1.0.2"

import asyncio

from .other.auxiliary_code.base_bot_test_case_class import BaseBotTestCase
from prototypes.telegram_scripts.bot_state_handlers import *


# ____________________________________________________________________________
class TestOnStartUpPositive(BaseBotTestCase):
    async def asyncSetUp(self) -> None:
        await BaseBotTestCase.asyncSetUp(self=self)

        self.dispatcher.startup.register(callback=on_start_bot)

    # -------------------------------------------------------------------------
    async def test_successfully_activated_handler(self) -> None:
        test_task = self.event_loop.create_task(
            coro=self.dispatcher.start_polling(self.bot)  # type: ignore
        )

        try:
            async with asyncio.timeout(delay=15):
                await test_task
        except asyncio.TimeoutError:
            pass

        self.assertTrue(_current_state())


# _____________________________________________________________________________
class TestOnShutDownPositive(BaseBotTestCase):
    async def asyncSetUp(self) -> None:
        await BaseBotTestCase.asyncSetUp(self=self)

        self.dispatcher.shutdown.register(callback=on_stop_bot)
        _current_state.switch_state()

    # -------------------------------------------------------------------------
    async def test_successfully_activated_handler(self) -> None:
        test_task = self.event_loop.create_task(
            coro=self.dispatcher.start_polling(self.bot)  # type: ignore
        )

        try:
            async with asyncio.timeout(delay=15):
                await test_task
        except asyncio.TimeoutError:
            pass

        self.assertFalse(_current_state())
