# -*- coding: utf-8 -*-

"""
Module `test_json_handler`, a set of test cases used to control the performance
and quality of the `json_handler` module components.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__author__ = "4-proxy"
__version__ = "1.0.0"

import unittest

import os

from common.external_handling import json_handler

from typing import Dict


CURRENT_FILE_PATH: str = os.path.abspath(path=__file__)
CURRENT_DIR_PATH: str = os.path.dirname(p=CURRENT_FILE_PATH)
TEST_DATA_DIR_NAME: str = "test_data"
VALID_JSON_FILE_NAME: str = "valid_json_file.json"
INVALID_JSON_FILE_NAME: str = "invalid_json_file.json"


# _____________________________________________________________________________
class TestGetContentFromJsonPositive(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls._tested_json_file_path: str = os.path.join(
            CURRENT_DIR_PATH, TEST_DATA_DIR_NAME, VALID_JSON_FILE_NAME
        )

    # -------------------------------------------------------------------------
    def setUp(self) -> None:
        super().setUp()
        self.tested_function = json_handler.get_content_from_json
        self.tested_specific_type = json_handler.ContentJSON

    # -------------------------------------------------------------------------
    def test_function_accept_filepath(self) -> None:
        # Build
        test_filepath: str = self._tested_json_file_path

        # Check
        self.tested_function(test_filepath)

    # -------------------------------------------------------------------------
    def test_returns_specific_type(self) -> None:
        # Build
        test_filepath: str = self._tested_json_file_path
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
    def test_reads_json_file_content_correctly(self) -> None:
        # Build
        test_filepath: str = self._tested_json_file_path

        expected_data: Dict[str, str] = {
            "key": "banana",
            "author": "4-proxy",
            "credit_card_code": "123"
        }  # Must match the contents of the file to be tested.

        # Operate
        json_file_content = self.tested_function(test_filepath)

        # Check
        self.assertDictEqual(
            d1=json_file_content,
            d2=expected_data,
            msg="Failure! The contents of inspected dictionary didn't match the expected!"
        )


# _____________________________________________________________________________
class TestGetContentFromJsonNegative(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.tested_function = json_handler.get_content_from_json

    # -------------------------------------------------------------------------
    def test_FileNotFoundError_when_file_does_not_exist(self) -> None:
        # Build
        incorrect_filepath: str = os.path.join(
            CURRENT_DIR_PATH, TEST_DATA_DIR_NAME, "file_not_exist.json"
        )

        # Check
        with self.assertRaises(expected_exception=FileNotFoundError):
            # Operate
            self.tested_function(incorrect_filepath)

    # -------------------------------------------------------------------------
    def test_JSONDecodeError_on_invalid_json(self) -> None:
        from json import JSONDecodeError

        # Build
        not_json_filepath = os.path.join(
            CURRENT_DIR_PATH, TEST_DATA_DIR_NAME, INVALID_JSON_FILE_NAME
        )

        # Check
        with self.assertRaises(expected_exception=JSONDecodeError):
            # Operate
            self.tested_function(not_json_filepath)
