# -*- coding: utf-8 -*-

"""
The manual_test_bot_start_command_handler module is a manual test,
to test components of the bot_start_command_handler module.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__author__ = "4-proxy"
__version__ = "1.0.2"

import asyncio

from tests.tests_telegram_scripts.other.auxiliary_code.base_bot_test_case_class import (
    BaseBotTestCase,
)
from prototypes.telegram_scripts.bot_start_command_handler import (
    router,
    test_status,
)


# ____________________________________________________________________________
class TestStartCommand(BaseBotTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        BaseBotTestCase.setUpClass()

    # -------------------------------------------------------------------------
    async def asyncSetUp(self) -> None:
        await BaseBotTestCase.asyncSetUp(self=self)

        self.dispatcher.include_router(router=router)

    # -------------------------------------------------------------------------
    async def test_successfully_activated_handler(self) -> None:
        """
        To successfully pass the test, it is required - after launching the bot,
        personally write in the general chat command: `/start`, after that the bot will have to process it.
        """

        print(self.test_successfully_activated_handler.__doc__)

        test_task = self.event_loop.create_task(
            coro=self.dispatcher.start_polling(self.bot)  # type: ignore
        )

        try:
            async with asyncio.timeout(delay=15):
                await test_task

        except asyncio.TimeoutError:
            pass

        self.assertCountEqual(["OK"], test_status)


if __name__ == "__main__":
    import unittest

    unittest.main()
