# -*- coding: utf-8 -*-

"""
description

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = []

__author__ = "4-proxy"
__version__ = "0.1.0"

import unittest

import aiogram

from bot_handling import bot_handler

from typing import Dict, Union, Any


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
    async def test_returned_object_is_aiogram_dispatcher(self) -> None:
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
            "random_int_number": randint(a=0, b=999),
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
            with self.subTest(msg=f"Failure! Subtest {subtest_counter} is stopped!", pattern=(test_key, test_value)):
                self.assertEqual(
                    first=workflow.get(test_key),
                    second=test_value
                )
