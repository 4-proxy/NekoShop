# -*- coding: utf-8 -*-

"""
The `workflow_intermediary` module defines a data class
that facilitates the organization and transfer of data
necessary for the proper functioning of the application.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = ["WorkflowIntermediary"]

__author__ = "4-proxy"
__version__ = "0.1.3"

from dataclasses import dataclass

from aiogram import Bot


# _____________________________________________________________________________
@dataclass
class WorkflowIntermediary:
    """Mediator for data transfer.

    This data class is designed to store essential data and objects
    utilized in different parts of the application, ensuring seamless
    communication and operation.

    Attributes:
        current_bot (Bot): An instance of the Telegram bot.
        owner_chat_id (str): The chat ID of the bot owner.
    """
    current_bot: Bot
    owner_chat_id: str
