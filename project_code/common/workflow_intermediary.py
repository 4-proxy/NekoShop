# -*- coding: utf-8 -*-

"""
The `workflow_intermediary` module stores a dataclass
that will contain the actual objects and data
for the correct operation of the program code.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = ["WorkflowIntermediary"]

__author__ = "4-proxy"
__version__ = "0.1.0"

from dataclasses import dataclass

import aiogram


# _____________________________________________________________________________
@dataclass
class WorkflowIntermediary:
    """Mediator for data transfer.

    Data structure for storing actual data and objects
    that will be used in different parts of the program code.
    """
    current_bot: aiogram.Bot
    owner_chat_id: str
