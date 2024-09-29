# -*- coding: utf-8 -*-

"""
The `bot_config_handler` module is responsible for processing
and managing the configuration settings for a Telegram bot.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = ["BotConfigDTO"]

__author__ = "4-proxy"
__version__ = "1.1.1"

from dataclasses import dataclass


# _____________________________________________________________________________
@dataclass(frozen=True)
class BotConfigDTO:
    """Data structure for storing and representing the configuration of a Telegram bot.

    This class is immutable and contains essential attributes required for bot operation.

    Attributes:
        api_token (str): The API token used for authenticating the bot with the Telegram API.
        owner_chat_id (str): The unique identifier of the chat where the bot owner resides.
        debug (bool): A flag indicating whether the bot is running in debug mode, which may enable additional logging or features.
    """
    api_token: str
    owner_chat_id: str
    debug: bool
