# -*- coding: utf-8 -*-

"""
description

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = []

__author__ = "4-proxy"
__version__ = "0.2.0"

import unittest

import aiogram

from bot_handling import bot_handler

from typing import Dict, Union, Any, Optional


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
    async def test_returned_object_is_aiogram_Dispatcher(self) -> None:
        # Operate
        dispatcher: aiogram.Dispatcher = await self.tested_function()

        # Check
        self.assertIsInstance(
            obj=dispatcher,
            cls=aiogram.Dispatcher,
            msg=f"Failure! Inspected object is instance of incorrect class!"
        )

    # -------------------------------------------------------------------------
    async def test_accept_kwargs_into_workflow_data(self) -> None:
        from random import randint

        # Build
        test_data: Dict[str, Union[str, bool, int]] = {
            "author_name": "4-proxy",
            "debug_mode": True,
            "random_int_number": randint(a=0, b=999)
        }

        # Operate
        dispatcher: aiogram.Dispatcher = await self.tested_function(
            **test_data
        )

        # Check
        workflow: Dict[str, Any] = dispatcher.workflow_data

        subtest_counter: int = 0
        for test_key, test_value in test_data.items():
            subtest_counter += 1
            with self.subTest(msg=f"Failure! Subtest {subtest_counter} is stopped!",
                              pattern=(test_key, test_value)):
                self.assertEqual(
                    first=workflow.get(test_key),
                    second=test_value
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
    async def test_returned_object_is_aiogram_Bot(self) -> None:
        # Operate
        bot: aiogram.Bot = await self.tested_function(api_token=self._bot_api_token)

        # Check
        self.assertIsInstance(
            obj=bot,
            cls=aiogram.Bot,
            msg="Failure! Inspected object is instance of incorrect class!"
        )

    # -------------------------------------------------------------------------
    async def test_default_parse_mode_is_HTML(self) -> None:
        from aiogram.enums import ParseMode

        # Build
        bot: aiogram.Bot = await self.tested_function(api_token=self._bot_api_token)
        bot_parse_mode: Optional[str] = bot.default.parse_mode

        # Check
        self.assertEqual(
            first=bot_parse_mode,
            second=ParseMode.HTML,
            msg="Failure! Default parse mode of bot is not HTML!"
        )

    # -------------------------------------------------------------------------
    async def test_another_parse_mode_in_arguments(self) -> None:
        from aiogram.enums import ParseMode

        # Build
        expected_parse_mode = ParseMode.MARKDOWN

        # Operate
        bot: aiogram.Bot = await self.tested_function(
            api_token=self._bot_api_token,
            parse_mode=expected_parse_mode
        )

        bot_parse_mode: Optional[str] = bot.default.parse_mode

        # Check
        self.assertEqual(
            first=bot_parse_mode,
            second=expected_parse_mode,
            msg="Failure! Parse mode of bot is unexpected!"
        )


# _____________________________________________________________________________
class TestCreateBotNegative(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

    # -------------------------------------------------------------------------
    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()

        self.tested_function = bot_handler.create_bot

    # -------------------------------------------------------------------------
    @unittest.expectedFailure
    async def test_call_without_arguments(self) -> None:
        bot: aiogram.Bot = await self.tested_function()

    # -------------------------------------------------------------------------
    async def test_invalid_api_token_raise_TokenValidationError(self) -> None:
        """
        This check ensures the format of the string is correct.

        If it is not the `*:*` format, an exception `TokenValidationError` must be raised.
        If the token is in the `*:*` format but not valid in Telegram, it will be accepted.
        *Because the validity of the token in Telegram can only be verified by running the bot.
        """
        from aiogram.utils.token import TokenValidationError

        # Build
        invalid_api_token = "1234hello"

        # Check
        with self.assertRaises(expected_exception=TokenValidationError):
            bot: aiogram.Bot = await self.tested_function(api_token=invalid_api_token)
