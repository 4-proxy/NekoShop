# -*- coding: utf-8 -*-

__all__: list[str] = ["BaseBotTestCase"]

import unittest
import asyncio
import aiogram

from ..config import TestCaseConfig as Config


# ____________________________________________________________________________
class BaseBotTestCase(unittest.IsolatedAsyncioTestCase):
    """BaseTestCase base class, for testing bot functionality.

    The base class eliminates code duplication in test case settings,
    provides simple configuration and preparation for bot launch.
    """

    @classmethod
    def setUpClass(cls) -> None:
        unittest.IsolatedAsyncioTestCase.setUpClass()

        cls._correct_bot_token: str = Config.API_TOKEN_BOT

    # -------------------------------------------------------------------------
    async def asyncSetUp(self) -> None:
        await unittest.IsolatedAsyncioTestCase.asyncSetUp(self=self)

        self.event_loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()

        self.bot: aiogram.Bot = aiogram.Bot(token=self._correct_bot_token)
        self.dispatcher: aiogram.Dispatcher = aiogram.Dispatcher()
