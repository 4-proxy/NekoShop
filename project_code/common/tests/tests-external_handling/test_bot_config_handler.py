# -*- coding: utf-8 -*-

"""
Module `test_bot_config_handler`, a set of test cases used to control the performance
and quality of the `bot_config_handler` module components.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__author__ = "4-proxy"
__version__ = "1.0.0"

import unittest

from common.external_handling import bot_config_handler

from typing import Tuple


# _____________________________________________________________________________
class TestBotConfig(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.tested_class = bot_config_handler.BotConfig

    # -------------------------------------------------------------------------
    def test_instance_creation_raises_TypeError(self) -> None:
        # Check
        with self.assertRaises(expected_exception=TypeError):
            # Operate
            self.tested_class()

    # -------------------------------------------------------------------------
    def test_expected_fields_are_present(self) -> None:
        # Build
        expected_fields: Tuple[str, ...] = (
            "API_TOKEN", "OWNER_CHAT_ID", "DEBUG"
        )

        for expected_field in expected_fields:
            with self.subTest(pattern=expected_field):
                # Check
                self.assertIn(
                    member=expected_field,
                    container=self.tested_class.__dataclass_fields__,
                    msg=f"The inspected class does not have a {expected_field} field!"
                )
