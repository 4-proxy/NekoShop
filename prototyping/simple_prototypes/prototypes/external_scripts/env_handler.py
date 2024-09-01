# -*- coding: utf-8 -*-

"""
The env_handler module is used to process environment configuration (.env) files,
to load [key : value] pairs into the virtual environment and provide additional functionality to interact with the loaded pairs.
additional functionality for interacting with the loaded pairs.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    "load_env_file",
    "get_key_value_from_environment",
    "normalize_env_value_type",
]

__author__ = "4-proxy"
__version__ = "1.0.1"

import os
import dotenv

from typing import Union


# ----------------------------------------------------------------------------
def load_env_file(filepath: str) -> bool:
    """load_env_file loads an '.env' file into the environment.

    The function loads [key : value] pairs from a file with the extension '.env',
    into the current virtual environment of the system.

    Args:
        filepath (str): path to the '.env' file.

    Raises:
        FileNotFoundError: Raises if the file does not exist.

    Returns:
        bool: Have keys been loaded into the virtual environment?
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found at the specified path: {filepath}")

    return dotenv.load_dotenv(dotenv_path=filepath)


# ----------------------------------------------------------------------------
def get_key_value_from_environment(key: str) -> str:
    """get_key_value_from_environment returns the key value from the environment.

    The function accesses the current virtual environment,
    to get the value for the requested key.

    Args:
        key (str): the requested key from the environment.

    Raises:
        ValueError: Raises if the key does not belong to the environment.

    Returns:
        str: the received value, based on the requested key.
    """
    value: Union[str, None] = os.environ.get(key)

    if value is None:
        raise KeyError(f"The {key} key does not exist in the current environment!")

    return value


# ----------------------------------------------------------------------------
def normalize_env_value_type(env_value: str) -> Union[str, int, bool]:
    """normalize_env_value_type normalizes the type of data in the string.

    The function determines the type of data contained in the string,
    and then returns the value using the correct data type.

    *When getting the key value from the virtual environment, the data type is a string.

    Args:
        env_value (str): string to normalize.

    Returns:
        Union[str, int, bool]: Supported types for normalization.
    """
    if env_value.isdigit():
        return int(env_value)
    elif env_value.lower() == "true":
        return True
    elif env_value.lower() == "false":
        return False

    return env_value
