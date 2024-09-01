# -*- coding: utf-8 -*-

"""
The `abstract_async_database` module provides a base abstract class,
which will represent the database.

Specific database implementations will inherit from this abstract class
and implement methods to work on a particular database (DBMS).

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = ["AbstractAsyncDataBase"]

__author__ = "4-proxy"
__version__ = "1.0.1"

from abc import ABC, abstractmethod

from typing import Any, Dict, Optional


# _____________________________________________________________________________
class AbstractAsyncDataBase[APIType, ConnectMethodType, ConnectionType](ABC):
    """AbstractAsyncDataBase class for representing a database.

    This class serves as the basis for the implementation of specific classes,
    that support connection to a particular type of database.
    It defines methods and attributes that must be
    implemented in derived classes to work on specific database types (DBMS).

    *The class must not support direct interaction over the database,
    for this purpose an API must be implemented and connected.

    Args:
        ABC: Base class for creating abstract classes,
             allowing to implement abstraction.

    Attributes:
        _connection_data (Dict[str, Any]): The data required to establish a connection to the database.
        _connect_method (ConnectMethodType): The function used to establish a connection to the database.
        _connection_with_database (Optional[ConnectionType]): An object representing the current connection to the database.
                                                              Defaults to None.
        api (APIType): An object that implements an API for working on a specific database type.
    """

    _connection_data: Dict[str, Any]
    _connect_method: ConnectMethodType
    _connection_with_database: Optional[ConnectionType] = None
    api: APIType

    # -------------------------------------------------------------------------
    def __init__(
        self,
        connect_method: ConnectMethodType,
        connection_data: Dict[str, Any],
        api: APIType,
    ) -> None:
        """__init__ constructor.

        Args:
            connect_method (ConnectMethodType): The function used to establish a connection to the database.
            connection_data (Dict[str, str]): The data used to set up the connection.
            api (APIType): An object that implements an API for a particular database type.
        """
        self._connect_method = connect_method
        self._connection_data = connection_data
        self.api = api

    # -------------------------------------------------------------------------
    @abstractmethod
    async def get_connect_method(self) -> ConnectMethodType:
        """get_connect_method returns a function to connect to the database.

        This method must return a function,
        that will be used to establish a connection to the database.

        Returns:
            ConnectMethodType: The function to connect to the database.
        """
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    async def create_connection_with_database(self) -> None:
        """create_connection_with_database establishes a connection to the database.

        This method must establish a connection to the database,
        using the method and data to create the connection.

        *The established connection should be assigned to the appropriate attribute.
        """
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    async def get_connection_with_database(self) -> ConnectionType:
        """get_connection_with_database returns a database connection object.

        This method must return a database connection object.

        *If the connection has not been established before calling this method,
        the method should be called to establish the connection.

        Returns:
            ConnectionType: database connection object.
        """
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    async def close_connection_with_database(self) -> None:
        """close_connection_with_database closes the current database connection.

        This method must close the current database connection,
        which is assigned to the corresponding attribute.
        """
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    async def connect_api_to_database(self) -> None:
        """connect_api_to_database establishes the API connection to the database.

        This method should configure the connection of the installed API to the database,
        by calling the appropriate API method to configure it.
        """
        pass
