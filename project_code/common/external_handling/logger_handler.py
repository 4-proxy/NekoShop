# -*- coding: utf-8 -*-

"""
The `logger_handler` module is used to configure basic project logging.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    'create_log_directory_if_not_exists'
]

__author__ = "4-proxy"
__version__ = "1.0.0"

import logging

import os


LOG_FILENAME: str = "NekoShopApp.log"
LOG_DIR_NAME: str = "logs"
LOG_FILEPATH: str = os.path.join(LOG_DIR_NAME, LOG_FILENAME)

LOG_MESSAGE_FORMAT: str = "%(asctime)s | %(levelname)s | %(name)s > %(message)s"
LOG_DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"


# -----------------------------------------------------------------------------
def check_directory_exists(dirpath: str) -> bool:
    """Check if a directory exists at the specified path.

    This function checks whether a directory exists at the given `dirpath`.
    It uses the `os.path.isdir` method to determine if the path is a directory.

    Args:
        dirpath (str): The path of the directory to check.
                       This should be a string representing the file system path

    Returns:
        bool: True if the directory exists, False otherwise.

    Example:
        >>> check_directory_exists('/path/to/directory')
        True  # if the directory exists
        False # if the directory does not exist
    """
    is_exists: bool = os.path.isdir(s=dirpath)

    return is_exists


# -----------------------------------------------------------------------------
def create_log_directory_if_not_exists() -> None:
    """Create a log directory if it does not already exist.

    This function checks for the existence of the directory defined by the
    constant `LOG_DIR_NAME`. If the directory does not exist, it will be created
    using `os.makedirs`.

    Raises:
        OSError: If an error occurred while creating the directory, such as
                 permission issues or invalid path.

    Example:
        >>> create_log_directory_if_not_exists()
        # This will create the directory if it does not exist.
    """
    is_exists: bool = check_directory_exists(dirpath=LOG_DIR_NAME)

    if is_exists is False:
        os.makedirs(LOG_DIR_NAME)


if __name__ != '__main__':
    create_log_directory_if_not_exists()

    logging.basicConfig(
        filename=LOG_FILEPATH,
        level=logging.NOTSET,
        format=LOG_MESSAGE_FORMAT,
        datefmt=LOG_DATE_FORMAT
    )
