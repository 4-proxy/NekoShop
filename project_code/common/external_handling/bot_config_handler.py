# -*- coding: utf-8 -*-

"""
The `bot_config_handler` module is used to process
and present configuration for Telegram bot.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = ["BotConfigDTO"]

__author__ = "4-proxy"
__version__ = "1.0.1"

from dataclasses import dataclass

from typing import NoReturn


# _____________________________________________________________________________
@dataclass
class BotConfigDTO:
    """
    Data structure for storing bot configuration.

    Attributes:
        API_TOKEN (str): API token for bot access.
        OWNER_CHAT_ID (str): The chat identifier of the bot owner.
        DEBUG (bool): Flag indicating whether debug mode is enabled.

    Raises:
        TypeError: Raises when trying to create an instance of the class.
    """
    API_TOKEN: str
    OWNER_CHAT_ID: str
    DEBUG: bool

    def __init__(self, *args, **kwargs) -> NoReturn:
        """
        Prohibit the creation of instances of this class.

        Raises:
            TypeError: Always raises when trying to create an instance.
        """
        raise TypeError("Creating instances of this class is inadmissible!")
