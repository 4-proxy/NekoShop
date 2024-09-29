# -*- coding: utf-8 -*-

"""
The `json_handler` module is used to process JSON files.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    "parse_content_from_json",
    "ContentJSON"
]

__author__ = "4-proxy"
__version__ = "2.0.0"

import json

from typing import Dict, Any, NewType


ContentJSON = NewType('ContentJSON', Dict[str, Any])


# -----------------------------------------------------------------------------
def parse_content_from_json(filepath: str) -> ContentJSON:
    """Parse content from a JSON file.

    This function reads a JSON file from the specified file path and
    parses its content into a Python dictionary. The resulting dictionary
    is wrapped in a custom type `ContentJSON`.

    Args:
        filepath (str): The path to the `.json` file to be read.

    Returns:
        ContentJSON: The parsed content of the `.json` file as a dictionary.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file content is not valid JSON.
    """
    with open(file=filepath, mode='r') as json_file:
        file_content: Any = json.load(fp=json_file)

    return ContentJSON(file_content)
