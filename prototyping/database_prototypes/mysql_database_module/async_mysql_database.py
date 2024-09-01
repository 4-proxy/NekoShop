# -*- coding: utf-8 -*-

"""
The `async_mysql_database` module implements a class,
which provides an abstraction for working with a MySQL database. 

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = ["AsyncMySQLDataBase"]

__author__ = "4-proxy"
__version__ = "1.0.1"

from ..database_module.abstract_async_database import AbstractAsyncDataBase

from typing import Dict, Any
from mysql.connector.pooling import MySQLConnectionPool

from .async_mysql_database_api import AsyncMySQLAPI
from .types import AsyncMySQLConnectionType, AsyncMySQLConnectMethodType


# _____________________________________________________________________________
class AsyncMySQLDataBase(
    AbstractAsyncDataBase[
        AsyncMySQLAPI, AsyncMySQLConnectMethodType, AsyncMySQLConnectionType
    ]
):
    """AsyncMySQLDataBase class for representing a DBMS-MySQL database.

    This class is used to represent a DBMS-MySQL database.
    It provides asynchronous methods for managing database connections and for API integration,
    which will be used to perform operations on the database.

    *This implementation of the parent class,
    is interpreted using connection pooling and single/independent connection.

    Args:
        AbstractAsyncDataBase: Base class for implementing a specific type of database.

    Attributes:
        __pool (AsyncMySQLConnectionPool): The active pool of connections to the database.
    """

    __pool: MySQLConnectionPool

    # -------------------------------------------------------------------------
    def __init__(
        self,
        connect_method: AsyncMySQLConnectMethodType,
        connection_data: Dict[str, Any],
        api: AsyncMySQLAPI,
        pool_name: str = "mysql_pool",
        pool_size: int = 3,
    ) -> None:
        """__init__ constructor.

        Initializes an instance of the AsyncMySQLDataBase class.

        Args:
            connect_method (AsyncMySQLConnectMethodType): The function used to connect to the database independently.
            connection_data (Dict[str, str]): Data used to authenticate connections to the database.
            api (AsyncMySQLAPI): API object for performing operations on the database.
            pool_name (str, optional): The name identifier of the connection pool.
                                       The default is “mysql_pool”.
            pool_size (int, optional): The size/number of available pool connections.
                                       The default is 3.
        """
        super().__init__(
            connect_method=connect_method,
            connection_data=connection_data,
            api=api,
        )

        self.__pool = MySQLConnectionPool(
            pool_name=pool_name, pool_size=pool_size, **connection_data
        )

    # -------------------------------------------------------------------------
    async def get_connect_method(self) -> AsyncMySQLConnectMethodType:
        """get_connect_method returns a function for a single connection to the database.

        This method returns the function,
        that will be used to connect a single/independent connection to the database.

        Returns:
            AsyncMySQLConnectMethodType: The function used to connect to the database.
        """
        return self._connect_method

    # -------------------------------------------------------------------------
    async def create_connection_with_database(self) -> None:
        """create_connection_with_database establishes an independent connection to the database.

        This method creates a separate/independent connection from the pool,
        using the assigned method and data.

        *The established connection is stored in the `_connection_with_database` attribute.
        """
        connect_method: AsyncMySQLConnectMethodType = (
            await self.get_connect_method()
        )

        connection: AsyncMySQLConnectionType = await connect_method(
            **self._connection_data
        )

        self._connection_with_database = connection

    # -------------------------------------------------------------------------
    async def get_connection_with_database(self) -> AsyncMySQLConnectionType:
        """get_connection_with_database returns an independent database connection object.

        This method returns the object of the current,
        database connection independent from the connection pool.

        *If the connection has not been created,
        then the corresponding method is called to create the database connection.

        Returns:
            AsyncMySQLConnectionType: DB Connection Object.
        """
        if self._connection_with_database is None:
            await self.create_connection_with_database()

        return self._connection_with_database  # type: ignore

    # -------------------------------------------------------------------------
    async def close_connection_with_database(self) -> None:
        """close_connection_with_database closes the current independent connection to the database.

        This method closes the current independent connection to the database from the connection pool,
        connection to the database, thus terminating the independent connection to the database.
        """
        connection: AsyncMySQLConnectionType = (
            await self.get_connection_with_database()
        )

        await connection.close()

    # -------------------------------------------------------------------------
    async def connect_api_to_database(self) -> None:
        """connect_api_to_database sets up the API connection to the database.

        This method configures the API connection to the database,
        passing a connection pool and an independent connection,
        allowing the API to communicate over the database.
        """
        pool: MySQLConnectionPool = self.__pool
        connection_with_database: AsyncMySQLConnectionType = (
            await self.get_connection_with_database()
        )

        await self.api.set_up(
            separate_connection=connection_with_database, pool=pool
        )
