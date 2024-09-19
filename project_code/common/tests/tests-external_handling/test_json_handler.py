# -*- coding: utf-8 -*-

"""
description

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__author__ = "4-proxy"
__version__ = "0.1.1"

import unittest

from common.external_handling import json_handler

from typing import Dict


# _____________________________________________________________________________
class TestGetContentFromJsonPositive(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        import os

        super().setUpClass()

        current_dir: str = os.path.dirname(p=os.path.abspath(path=__file__))

        cls._test_json_file_path: str = os.path.join(
            current_dir, "test_data", "test_json_file.json"
        )

    # -------------------------------------------------------------------------
    def setUp(self) -> None:
        super().setUp()

        self.tested_function = json_handler.get_content_from_json
        self.tested_specific_type = json_handler.ContentJSON

    # -------------------------------------------------------------------------
    def test_function_accept_filepath(self) -> None:
        # Build
        test_filepath: str = self._test_json_file_path

        # Check
        self.tested_function(test_filepath)

    # -------------------------------------------------------------------------
    def test_returned_object_is_specific_type(self) -> None:
        # Build
        test_filepath: str = self._test_json_file_path
        expected_type = self.tested_specific_type

        # Operate
        test_object = self.tested_function(test_filepath)

        # Check
        self.assertIsInstance(
            obj=test_object,
            cls=expected_type,
            msg=f"Failure! Inspected object is not instance of {expected_type}!"
        )

    # -------------------------------------------------------------------------
    def test_correct_reading_json_file_content(self) -> None:
        # Build
        test_filepath: str = self._test_json_file_path

        test_data: Dict[str, str] = {
            "key": "banana",
            "author": "4-proxy",
            "credit_card_code": "123"
        }  # Must match the contents of the file to be tested.

        # Operate
        json_file_content = self.tested_function(test_filepath)

        # Check
        subtest_counter: int = 0
        for test_key, test_value in test_data.items():
            subtest_counter += 1
            with self.subTest(msg=f"Failure! Subtest {subtest_counter} is stopped!",
                              pattern=(test_key, test_value)):
                self.assertEqual(first=json_file_content.get(test_key),
                                 second=test_value)


# _____________________________________________________________________________
class TestGetContentFromJsonNegative(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.tested_function = json_handler.get_content_from_json

    # -------------------------------------------------------------------------
    def test_if_file_not_exist_raise_FileNotFound(self) -> None:
        import os

        # Build
        current_dir: str = os.path.dirname(p=os.path.abspath(path=__file__))

        incorrect_filepath: str = os.path.join(
            current_dir, "test_data", "file_not_exist.json"
        )

        # Check
        with self.assertRaises(expected_exception=FileNotFoundError):
            # Operate
            self.tested_function(incorrect_filepath)
