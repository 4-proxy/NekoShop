# -*- coding: utf-8 -*-

"""
The `async_sql_database_api` module provides a generic interface,
which defines methods to implement APIs for specific database types,
using a single asynchronous connection.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = ["AsyncSQLDataBaseAPI"]

__author__ = "4-proxy"
__version__ = "1.0.1"

from abc import ABC, abstractmethod

from typing import Dict
from string import Template


# _____________________________________________________________________________
class AsyncSQLDataBaseAPI[ConnectionType](ABC):
    """AsyncSQLDataBaseAPI interface to implement an API for working on the database.

    This class provides an interface,
    containing a set of asynchronous methods for implementing specific API types,
    designed to perform operations on specific database types.

    *The interface assumes working on a single connection providing connection to the database.
    This connection must support asynchrony.

    Args:
        ABC: A base class for creating abstract classes,
             allowing to realize abstraction.
    """

    @abstractmethod
    async def set_connection_with_database(
        self, connection: ConnectionType
    ) -> None:
        """set_connection_with_database sets the connection to the database for the API.

        This method must set the received connection to the database,
        to the appropriate API attribute that is responsible for storing the connection.

        Args:
            connection (ConnectionType): The object of the connection to the database.
        """
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    async def get_connection_with_database(self) -> ConnectionType:
        """get_connection_with_database returns the connection to the database.

        This method should return a connection object,
        which provides a connection to the database and will allow the API to perform manipulations on the database.

        Returns:
            ConnectionType: Database Connection Object.
        """
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    async def check_connection_with_database(self) -> bool:
        """check_connection_with_database checks for database connection activity.

        This method should perform a check that determines,
        whether the current connection to the database is active.

        Returns:
            bool: True if the connection is active; otherwise False.
        """
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    async def execute_sql_query_to_database(
        self, query_template: Template, query_data: Dict[str, str]
    ) -> None:
        """execute_sql_query_to_database executes a query against a database.

        This method should execute a query against the connected database.
        Getting the query as a string and the data to substitute into the query.

        Args:
            query_template (Template): query_template.
            query_data (Dict[str, str]): The data to substitute into the query.
        """
        pass
