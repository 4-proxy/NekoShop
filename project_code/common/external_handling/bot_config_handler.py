# -*- coding: utf-8 -*-

"""
description

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = ["BotConfig"]

__author__ = "4-proxy"
__version__ = "0.1.0"

from dataclasses import dataclass

from typing import NoReturn


# _____________________________________________________________________________
@dataclass
class BotConfig:
    API_TOKEN: str
    OWNER_CHAT_ID: str
    DEBUG: bool

    def __new__(cls) -> NoReturn:
        raise TypeError("Creating instances of this class is inadmissible")
