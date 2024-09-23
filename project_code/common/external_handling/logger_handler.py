# -*- coding: utf-8 -*-

"""
description

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    "LOG_FILENAME",
    "LOG_DIR_NAME",
    "LOG_FILEPATH"
]

__author__ = "4-proxy"
__version__ = "0.1.0"

import logging

import os


LOG_FILENAME: str = "NekoShopApp.log"
LOG_DIR_NAME: str = "logs"
LOG_FILEPATH: str = os.path.join(LOG_DIR_NAME, LOG_FILENAME)


logging.basicConfig(filename=LOG_FILEPATH,
                    level=logging.NOTSET)
