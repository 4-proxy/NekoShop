# -*- coding: utf-8 -*-

"""
The `async_mysql_database_api` module provides a class representing the API,
for interacting with the database, DBMS-MySQL.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = ["AsyncMySQLAPI"]

__author__ = "4-proxy"
__version__ = "1.0.1"

from ..database_module.async_sql_database_api import (
    AsyncSQLDataBaseAPI,
)
from ..database_module.async_sql_database_pool_api import (
    AsyncSQLDataBasePoolAPI,
)

from typing import Dict
from string import Template
from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector.errors import Error as MySQLError

from .types import (
    AsyncMySQLConnectionType,
    MySQLPooledConnection,
)


class AsyncMySQLAPI(
    AsyncSQLDataBaseAPI[AsyncMySQLConnectionType],
    AsyncSQLDataBasePoolAPI[MySQLConnectionPool, MySQLPooledConnection],
):
    """AsyncMySQLAPI class to represent the API for a RDBMS-MySQL database.

    This class is designed to represent the API.
    It provides asynchronous methods to manage pool connections and independent connection to the database.

    The *Independent connection is used for direct connection to the database.
    The connection pool is used to query the application using this API.

    Args:
        AsyncSQLDataBaseAPI: Interface for implementing the single connection API.
        AsyncSQLDataBasePoolAPI: Interface to implement the connection pool API.

    Attributes:
        __pool (AsyncMySQLConnectionPool): The active database connection pool
        __connection_with_database (AsyncMySQLConnectionType): Active independent connection to the database.
    """

    __pool: MySQLConnectionPool
    __connection_with_database: AsyncMySQLConnectionType

    async def set_up(
        self,
        separate_connection: AsyncMySQLConnectionType,
        pool: MySQLConnectionPool,
    ) -> None:
        """set_up configures the API.

        This method is used for the initial configuration of the API.
        Calling the appropriate methods to set independent and pool connections.

        Args:
            separate_connection (AsyncMySQLConnectionType): Independent connection to the database.
            pool (MySQLConnectionPool): A pool of connections to the database.
        """
        await self.set_connection_with_database(connection=separate_connection)
        await self.set_connection_to_pool(pool=pool)

    # -------------------------------------------------------------------------
    async def set_connection_to_pool(self, pool: MySQLConnectionPool) -> None:
        """set_connection_to_pool connects the connection pool to the API.

        This method sets the received connection pool to the database,
        to the corresponding API attribute responsible for storing the connection pool.

        Args:
            pool (MySQLConnectionPool): The database connection pool.
        """
        self.__pool = pool

    # -------------------------------------------------------------------------
    async def set_connection_with_database(
        self, connection: AsyncMySQLConnectionType
    ) -> None:
        """set_connection_with_database sets the connection to the database for the API.

        This method sets the connection to the database,
        to the corresponding API attribute responsible for storing the independent connection.

        Args:
            connection (AsyncMySQLConnectionType): Independent connection to the database.
        """
        self.__connection_with_database = connection

    # -------------------------------------------------------------------------
    async def get_connection_with_database(self) -> AsyncMySQLConnectionType:
        """get_connection_with_database returns an independent connection to the database.

        This method returns an independent connection object,
        set in the corresponding API attribute.

        *Independent connection is asynchronous.

        Returns:
            AsyncMySQLConnectionType: Database connection object.
        """
        return self.__connection_with_database

    # -------------------------------------------------------------------------
    async def get_connection_from_pool(self) -> MySQLPooledConnection:
        """get_connection_from_pool returns a database connection object from the pool.

        This method returns a connection object from the pool.

        *Pool connections, are synchronous.

        Returns:
            MySQLPooledConnection: database connection object from the pool.
        """
        connection: MySQLPooledConnection = self.__pool.get_connection()

        return connection

    # -------------------------------------------------------------------------
    async def check_connection_with_database(self) -> bool:
        """check_connection_with_database checks for direct database connection activity.

        This method performs a check
        to determine whether the current independent connection to the database is active.

        Returns:
            bool: True if the connection is active; otherwise False.
        """
        connection: AsyncMySQLConnectionType = (
            await self.get_connection_with_database()
        )

        connection_status: bool = await connection.is_connected()

        return connection_status

    # -------------------------------------------------------------------------
    async def close_connection_from_pool(
        self, connection: MySQLPooledConnection
    ) -> None:
        """close_connection_from_pool closes the connection from the pool.

        This method closes the specified connection to the database,
        returning the connection back to the pool.

        Args:
            connection (MySQLPooledConnection): pooled connection object.
        """
        connection.close()

    # -------------------------------------------------------------------------
    async def execute_sql_query_use_pool(
        self,
        query_template: Template,
        query_data: Dict[str, str],
    ) -> None:
        """execute_sql_query_use_pool executes a database query.

        This method executes a query to the database using a connection from the pool.
        The query template and the data to be substituted into the query are used to generate the query.

        Args:
            query_template (Template): query string template.
            query_data (Dict[str, str]): Data to substitute into the template.
        """
        connection: MySQLPooledConnection = (
            await self.get_connection_from_pool()
        )

        query_string: str = query_template.substitute(**query_data)

        try:
            with connection.cursor() as cursor:
                cursor.execute(query_string)

                connection.commit()

        except MySQLError as error:
            connection.rollback()
            print(f"An error occurred while executing a query! {error}")

        finally:
            await self.close_connection_from_pool(connection=connection)

    # -------------------------------------------------------------------------
    async def execute_sql_query_to_database(
        self, query_template: Template, query_data: Dict[str, str]
    ) -> None:
        """execute_sql_query_to_database executes a query to the database.

        This method executes a query to the database using an independent connection.
        The query template and the data to be substituted into the query are used to generate the query.

        Args:
            query_template (Template): query string template.
            query_data (Dict[str, str]): The data to substitute into the template.
        """
        connection: AsyncMySQLConnectionType = (
            await self.get_connection_with_database()
        )

        query_string: str = query_template.substitute(**query_data)

        try:
            async with await connection.cursor() as cursor:
                await cursor.execute(query_string)

                await connection.commit()

        except MySQLError as error:
            await connection.rollback()
            print(f"An error occurred while executing a query! {error}")
