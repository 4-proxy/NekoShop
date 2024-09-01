# -*- coding: utf-8 -*-

"""
The bot_state_handlers module is used to demonstrate the operation of bot state handlers.
bot state handlers.
(Direct use of this module in the development of the final product is not provided).

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = ["on_start_bot", "on_stop_bot", "_current_state"]

__author__ = "4-proxy"
__version__ = "1.0.1"


# ____________________________________________________________________________
class BotState:
    def __init__(self) -> None:
        self.__state: bool = False

    # -------------------------------------------------------------------------
    @property
    def state(self) -> bool:
        return self.__state

    # -------------------------------------------------------------------------
    @state.setter
    def state(self, new_state: bool) -> None:
        self.__state = new_state

    # -------------------------------------------------------------------------
    def switch_state(self) -> None:
        self.state = False if self.state else True

    # -------------------------------------------------------------------------
    def __call__(self) -> bool:
        return self.state


_current_state = BotState()


# ----------------------------------------------------------------------------
async def on_start_bot() -> None:
    _current_state.switch_state()


# ----------------------------------------------------------------------------
async def on_stop_bot() -> None:
    _current_state.switch_state()
