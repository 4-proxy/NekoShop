# -*- coding: utf-8 -*-

"""
The `async_sql_database_pool_api` module provides a generic interface,
which defines methods to implement APIs for specific database types,
using connection pooling.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = ["AsyncSQLDataBasePoolAPI"]

__author__ = "4-proxy"
__version__ = "1.0.1"

from abc import ABC, abstractmethod

from typing import Dict
from string import Template


# _____________________________________________________________________________
class AsyncSQLDataBasePoolAPI[PoolType, PooledConnectionType](ABC):
    """AsyncSQLDataBasePoolAPI interface to implement an API for database manipulation.

    This abstract class provides an interface
    containing a set of general methods requiring implementation for specific APIs,
    designed to perform operations on specific database types,
    using connection pooling.

    *The interface assumes operation using a connection pool to connect to the database.

    Args:
        ABC: A base class for creating abstract classes,
             allowing to realize abstraction.
    """

    @abstractmethod
    async def set_connection_to_pool(self, pool: PoolType) -> None:
        """set_connection_to_pool sets the connection to the pool for the API.

        This method shall set the received connection pool,
        to the appropriate API attribute that is responsible for storing the pool.

        Args:
            pool (PoolType): A connection pool object.
        """
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    async def get_connection_from_pool(self) -> PooledConnectionType:
        """get_connection_from_pool returns database connections from the pool.

        This method should return a connection from the pool,
        assigned to the API.

        Returns:
            PooledConnectionType: The object of the connection to the database from the pool.
        """
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    async def close_connection_from_pool(
        self, connection: PooledConnectionType
    ) -> None:
        """close_connection_from_pool closes the connection from the pool.

        This method should close the specified connection to the database,
        releasing the associated resources, returning the connection back to the pool.

        Returns:
            connection (PooledConnectionType): The connection object to close.
        """
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    async def execute_sql_query_use_pool(
        self,
        query_template: Template,
        query_data: Dict[str, str],
    ) -> None:
        """execute_sql_query_use_pool executes a database query.

        This method should execute a query against the database using a connection from the pool.
        As well as receiving the query as a string template and data to substitute into the query.

        Args:
            query_template (Template): query template.
            query_data (Dict[str, str]): The data to substitute into the query.
        """
        pass
