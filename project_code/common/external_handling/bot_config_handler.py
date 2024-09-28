# -*- coding: utf-8 -*-

"""
The `bot_config_handler` module is used to process
and present configuration for Telegram bot.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = ["BotConfigDTO"]

__author__ = "4-proxy"
__version__ = "1.1.0"

from dataclasses import dataclass


# _____________________________________________________________________________
@dataclass(frozen=True)
class BotConfigDTO:
    """
    Data structure for storing bot configuration.

    Attributes:
        api_token (str): API token for bot access.
        owner_chat_id (str): The chat identifier of the bot owner.
        debug (bool): Flag indicating whether debug mode is enabled.
    """
    api_token: str
    owner_chat_id: str
    debug: bool
