# -*- coding: utf-8 -*-

"""
description

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__author__ = "4-proxy"
__version__ = "0.2.0"

import unittest

import logging
import os

import common.external_handling.logger_handler as logger_handler


# _____________________________________________________________________________
class TestLoggerHandler(unittest.TestCase):
    EXPECTED_LOG_FILENAME: str = "NekoShopApp.log"
    EXPECTED_LOG_DIR_NAME: str = "logs"
    EXPECTED_LOG_FILEPATH: str = os.path.join(EXPECTED_LOG_DIR_NAME,
                                              EXPECTED_LOG_FILENAME)
    EXPECTED_LOG_MESSAGE_FORMAT: str = "%(asctime)s | %(levelname)s > %(message)s"
    EXPECTED_LOG_DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"

    # -------------------------------------------------------------------------
    def test_logger_file_name_is_correct(self) -> None:
        # Check
        self.assertEqual(first=logger_handler.LOG_FILENAME,
                         second=self.EXPECTED_LOG_FILENAME)

    # -------------------------------------------------------------------------
    def test_logger_directory_name_is_correct(self) -> None:
        # Check
        self.assertEqual(first=logger_handler.LOG_DIR_NAME,
                         second=self.EXPECTED_LOG_DIR_NAME)

    # -------------------------------------------------------------------------
    def test_logger_filepath_is_correct(self) -> None:
        # Check
        self.assertEqual(first=logger_handler.LOG_FILEPATH,
                         second=self.EXPECTED_LOG_FILEPATH)

    # -------------------------------------------------------------------------
    def test_default_level_of_logger_is_NOTSET(self) -> None:
        # Build
        expected_level = logging.NOTSET

        # Operate
        logger: logging.Logger = logging.getLogger()

        # Check
        self.assertEqual(first=logger.level,
                         second=expected_level)

    # -------------------------------------------------------------------------
    def test_logger_message_format_is_as_expected(self) -> None:
        # Check
        self.assertEqual(first=logger_handler.LOG_MESSAGE_FORMAT,
                         second=self.EXPECTED_LOG_MESSAGE_FORMAT)

    # -------------------------------------------------------------------------
    def test_logger_date_format_is_as_expected(self) -> None:
        # Check
        self.assertEqual(first=logger_handler.LOG_DATE_FORMAT,
                         second=self.EXPECTED_LOG_DATE_FORMAT)
