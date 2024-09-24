# -*- coding: utf-8 -*-

"""
The `logger_handler` module is used to configure basic project logging.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    "LOG_FILENAME",
    "LOG_DIR_NAME",
    "LOG_FILEPATH",
    "LOG_MESSAGE_FORMAT",
    "LOG_DATE_FORMAT"
]

__author__ = "4-proxy"
__version__ = "0.2.1"

import logging

import os


LOG_FILENAME: str = "NekoShopApp.log"
LOG_DIR_NAME: str = "logs"
LOG_FILEPATH: str = os.path.join(LOG_DIR_NAME, LOG_FILENAME)

LOG_MESSAGE_FORMAT: str = "%(asctime)s | %(levelname)s > %(message)s"
LOG_DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"


logging.basicConfig(
    filename=LOG_FILEPATH,
    level=logging.NOTSET,
    format=LOG_MESSAGE_FORMAT,
    datefmt=LOG_DATE_FORMAT
)
