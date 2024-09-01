# -*- coding: utf-8 -*-

"""
The module is designed to store custom types,
to ensure correct annotation in the code used.
"""

__all__: list[str] = [
    "AsyncMySQLConnectionType",
    "AsyncMySQLConnectMethodType",
    "MySQLPooledConnection",
]

from typing import Callable, Union, Coroutine, Any

from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.connection_cext import CMySQLConnection
from mysql.connector.aio.connection import MySQLConnection
from mysql.connector.aio.abstracts import MySQLConnectionAbstract


# Annotation for the type of independent asynchronous connection to MySQL.
AsyncMySQLConnectionType = Union[MySQLConnection, MySQLConnectionAbstract]

# Annotation for the function used to establish an asynchronous connection to MySQL.
AsyncMySQLConnectMethodType = Callable[
    ..., Coroutine[Any, Any, AsyncMySQLConnectionType]
]

# Annotation for the connection type from the pool to MySQL.
MySQLPooledConnection = Union[PooledMySQLConnection, CMySQLConnection]
