# -*- coding: utf-8 -*-

"""
Module `test_bot_state_handler`, a set of test cases used to control the performance
and quality of the `bot_state_handler` module components.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__author__ = "4-proxy"
__version__ = "1.1.0"

import unittest

import unittest.mock as UnitMock

from common.bot_handling import bot_state_handler
from common.workflow_intermediary import WorkflowIntermediary


# _____________________________________________________________________________
class TestBotStateHandler(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls._WorkflowData = WorkflowIntermediary

    # -------------------------------------------------------------------------
    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()
        self.tested_function_startup = bot_state_handler.on_startup
        self.tested_function_shutdown = bot_state_handler.on_shutdown

    # -------------------------------------------------------------------------
    @UnitMock.patch("aiogram.Bot", new_callable=UnitMock.AsyncMock)
    async def test_send_message_to_owner_at_startup(self,
                                                    MockBot: UnitMock.AsyncMock) -> None:
        # Build
        test_bot: UnitMock.AsyncMock = MockBot.return_value
        expected_chat_id = "123456789"
        expected_message_text = "I'am wake up!"

        self._WorkflowData.current_bot = test_bot
        self._WorkflowData.owner_chat_id = expected_chat_id

        # Operate
        await self.tested_function_startup()

        # Check
        test_bot.send_message.assert_called_once_with(chat_id=expected_chat_id,
                                                      text=expected_message_text)

    # -------------------------------------------------------------------------
    @UnitMock.patch("aiogram.Bot", new_callable=UnitMock.AsyncMock)
    async def test_send_message_to_owner_at_shutdown(self,
                                                     MockBot: UnitMock.AsyncMock) -> None:
        # Build
        test_bot: UnitMock.AsyncMock = MockBot.return_value
        expected_chat_id = "987654321"
        expected_message_text = "I'am go to sleep!"

        self._WorkflowData.current_bot = test_bot
        self._WorkflowData.owner_chat_id = expected_chat_id

        # Operate
        await self.tested_function_shutdown()

        # Check
        test_bot.send_message.assert_called_once_with(chat_id=expected_chat_id,
                                                      text=expected_message_text)

    # -------------------------------------------------------------------------
    async def test_logger_name_is_module_name(self) -> None:
        # Build
        expected_logger_name: str = bot_state_handler.__name__

        logger_name: str = bot_state_handler.logger.name

        # Check
        self.assertEqual(first=logger_name,
                         second=expected_logger_name)

    # -------------------------------------------------------------------------
    @UnitMock.patch("aiogram.Bot", new_callable=UnitMock.AsyncMock)
    @UnitMock.patch.object(target=bot_state_handler.logger,
                           attribute="info", autospec=True)
    async def test_logger_info_message_on_startup(self,
                                                  mock_logger_info: UnitMock.MagicMock,
                                                  MockBot: UnitMock.AsyncMock) -> None:
        # Build
        expected_message_text = "Bot is online!"
        fake_bot: UnitMock.AsyncMock = MockBot.return_value
        fake_chat_id = "987654321"

        self._WorkflowData.current_bot = fake_bot
        self._WorkflowData.owner_chat_id = fake_chat_id

        # Operate
        await self.tested_function_startup()

        # Check
        mock_logger_info.assert_called_once_with(expected_message_text)

    # -------------------------------------------------------------------------
    @UnitMock.patch("aiogram.Bot", new_callable=UnitMock.AsyncMock)
    @UnitMock.patch.object(target=bot_state_handler.logger,
                           attribute="info", autospec=True)
    async def test_logger_info_message_on_shutdown(self,
                                                   mock_logger_info: UnitMock.MagicMock,
                                                   MockBot: UnitMock.AsyncMock) -> None:
        # Build
        expected_message_text = "Bot is shutdown!"
        fake_bot: UnitMock.AsyncMock = MockBot.return_value
        fake_chat_id = "987654321"

        self._WorkflowData.current_bot = fake_bot
        self._WorkflowData.owner_chat_id = fake_chat_id

        # Operate
        await self.tested_function_shutdown()

        # Check
        mock_logger_info.assert_called_once_with(expected_message_text)
