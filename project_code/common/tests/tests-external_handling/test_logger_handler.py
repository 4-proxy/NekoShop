# -*- coding: utf-8 -*-

"""
description

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__author__ = "4-proxy"
__version__ = "0.1.0"

import unittest

import logging
import os

import common.external_handling.logger_handler as logger_handler


EXPECTED_LOG_FILENAME: str = "NekoShopApp.log"
EXPECTED_LOG_DIR_NAME: str = "logs"
EXPECTED_LOG_FILEPATH: str = os.path.join(EXPECTED_LOG_DIR_NAME,
                                          EXPECTED_LOG_FILENAME)


# _____________________________________________________________________________
class TestLoggerHandler(unittest.TestCase):
    def test_logger_file_name_is_correct(self) -> None:
        # Check
        self.assertEqual(first=logger_handler.LOG_FILENAME,
                         second=EXPECTED_LOG_FILENAME)

    # -------------------------------------------------------------------------
    def test_logger_directory_name_is_correct(self) -> None:
        # Check
        self.assertEqual(first=logger_handler.LOG_DIR_NAME,
                         second=EXPECTED_LOG_DIR_NAME)

    # -------------------------------------------------------------------------
    def test_logger_filepath_is_correct(self) -> None:
        # Check
        self.assertEqual(first=logger_handler.LOG_FILEPATH,
                         second=EXPECTED_LOG_FILEPATH)

    # -------------------------------------------------------------------------
    def test_default_level_of_logger_is_NOTSET(self) -> None:
        # Build
        expected_level = logging.NOTSET

        # Operate
        logger: logging.Logger = logging.getLogger()

        # Check
        self.assertEqual(first=logger.level,
                         second=expected_level)
