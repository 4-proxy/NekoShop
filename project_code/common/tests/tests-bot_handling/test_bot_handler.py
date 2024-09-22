# -*- coding: utf-8 -*-

"""
Module `test_bot_handler`, a set of test cases used to control the performance
and quality of the `bot_handler` module components.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__author__ = "4-proxy"
__version__ = "1.1.0"

import unittest

import aiogram
import asyncio

from common.bot_handling import bot_handler

from typing import Dict, Any, Optional


# _____________________________________________________________________________
class TestCreateDispatcherPositive(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

    # -------------------------------------------------------------------------
    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()
        self.tested_function = bot_handler.create_dispatcher

    # -------------------------------------------------------------------------
    async def test_call_without_exception(self) -> None:
        await self.tested_function()

    # -------------------------------------------------------------------------
    async def test_call_without_arguments(self) -> None:
        await self.tested_function()

    # -------------------------------------------------------------------------
    async def test_returns_aiogram_Dispatcher(self) -> None:
        # Build
        dispatcher: aiogram.Dispatcher = await self.tested_function()
        expected_type = aiogram.Dispatcher

        # Check
        self.assertIsInstance(
            obj=dispatcher,
            cls=expected_type,
            msg="Failure! Inspected object is not instance of aiogram.Dispatcher!"
        )

    # -------------------------------------------------------------------------
    async def test_accepts_kwargs_into_workflow_data(self) -> None:
        from random import randint

        # Build
        expected_data: Dict[str, Any] = {
            "author_name": "4-proxy",
            "debug_mode": True,
            "random_int_number": randint(a=0, b=999)
        }

        # Operate
        dispatcher: aiogram.Dispatcher = await self.tested_function(**expected_data)

        # Check
        workflow: Dict[str, Any] = dispatcher.workflow_data

        self.assertDictEqual(
            d1=workflow,
            d2=expected_data,
            msg="Failure! The contents of inspected dictionary didn't match the expected!"
        )


# _____________________________________________________________________________
class TestCreateBotPositive(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        from .test_data.bot_token import TOKEN

        super().setUpClass()
        cls._bot_api_token: str = TOKEN

    # -------------------------------------------------------------------------
    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()
        self.tested_function = bot_handler.create_bot

    # -------------------------------------------------------------------------
    async def test_call_without_exception(self) -> None:
        await self.tested_function(api_token=self._bot_api_token)

    # -------------------------------------------------------------------------
    async def test_returns_aiogram_Bot(self) -> None:
        # Build
        bot: aiogram.Bot = await self.tested_function(api_token=self._bot_api_token)
        expected_type = aiogram.Bot

        # Check
        self.assertIsInstance(
            obj=bot,
            cls=expected_type,
            msg="Failure! Inspected object is not instance of aiogram.Bot!"
        )

    # -------------------------------------------------------------------------
    async def test_default_parse_mode_is_HTML(self) -> None:
        from aiogram.enums import ParseMode

        # Build
        bot: aiogram.Bot = await self.tested_function(api_token=self._bot_api_token)

        # Check
        bot_parse_mode: Optional[str] = bot.default.parse_mode

        self.assertEqual(
            first=bot_parse_mode,
            second=ParseMode.HTML,
            msg="Failure! Default parse mode of bot is not HTML!"
        )

    # -------------------------------------------------------------------------
    async def test_accepts_custom_parse_mode(self) -> None:
        from aiogram.enums import ParseMode

        # Build
        expected_parse_mode = ParseMode.MARKDOWN

        # Operate
        bot: aiogram.Bot = await self.tested_function(api_token=self._bot_api_token,
                                                      parse_mode=expected_parse_mode)

        # Check
        bot_parse_mode: Optional[str] = bot.default.parse_mode

        self.assertEqual(
            first=bot_parse_mode,
            second=expected_parse_mode,
            msg="Failure! Parse mode of bot is unexpected!"
        )


# _____________________________________________________________________________
class TestCreateBotNegative(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()
        self.tested_function = bot_handler.create_bot

    # -------------------------------------------------------------------------
    async def test_invalid_api_token_format_raises_TokenValidationError(
            self) -> None:
        """
        This test ensures the format of the API token string is correct/valid.

        If it is not the `*:*` format, an exception `TokenValidationError` must be raised.
        If the token format is`*:*`, but not valid in Telegram, it will be accepted.
        *Because the validity of the token in Telegram can only be verified by running the bot.
        """
        from aiogram.utils.token import TokenValidationError

        # Build
        invalid_api_token = "1234hello"

        # Check
        with self.assertRaises(expected_exception=TokenValidationError):
            # Operate
            await self.tested_function(api_token=invalid_api_token)


# _____________________________________________________________________________
class TestRunBotPositive(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        from .test_data.bot_token import TOKEN

        super().setUpClass()
        cls._bot_api_token: str = TOKEN
        cls._invalid_api_token: str = "0000:xxxx"

    # -------------------------------------------------------------------------
    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()
        self.tested_function = bot_handler.run_bot

    # -------------------------------------------------------------------------
    async def test_successful_bot_launch(self) -> None:
        # Build
        async with aiogram.Bot(token=self._bot_api_token) as test_bot:
            test_dispatcher = aiogram.Dispatcher()
            test_delay: int = 10

            # Check
            with self.assertRaises(expected_exception=asyncio.TimeoutError):
                async with asyncio.timeout(delay=test_delay):
                    # Operate
                    await self.tested_function(bot=test_bot,
                                               dispatcher=test_dispatcher)

    # -------------------------------------------------------------------------
    async def test_accepts_aiogram_Bot_and_Dispatcher_as_key_parameters(
            self) -> None:
        # Build
        bot = aiogram.Bot(token=self._invalid_api_token)
        dispatcher = aiogram.Dispatcher()

        # Check
        with self.assertRaises(expected_exception=TypeError):
            # Operate
            await self.tested_function(bot, dispatcher)  # type: ignore


# _____________________________________________________________________________
class TestRunBotNegative(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls._invalid_api_token = "0000:xxxx"

    # -------------------------------------------------------------------------
    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()
        self.tested_function = bot_handler.run_bot

    # -------------------------------------------------------------------------
    async def test_invalid_api_token_raises_TelegramUnauthorizedError(
            self) -> None:
        from aiogram.exceptions import TelegramUnauthorizedError

        # Build
        test_bot = aiogram.Bot(token=self._invalid_api_token)
        test_dispatcher = aiogram.Dispatcher()

        # Check
        with self.assertRaises(expected_exception=TelegramUnauthorizedError):
            # Operate
            await self.tested_function(bot=test_bot,
                                       dispatcher=test_dispatcher)
