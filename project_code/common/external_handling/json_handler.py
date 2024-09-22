# -*- coding: utf-8 -*-

"""
The `json_handler` module is used to process JSON files.

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    "get_content_from_json",
    "ContentJSON"
]

__author__ = "4-proxy"
__version__ = "1.0.1"

import json

from typing import Dict, Any


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ContentJSON(Dict[str, Dict[str, Any]]):
    """ContentJSON type describing the content of JSON file."""
    pass


# -----------------------------------------------------------------------------
def get_content_from_json(filepath: str) -> ContentJSON:
    """get_content_from_json get JSON file content.

    This function reads a JSON file from the specified file path and
    parses its content into a Python dictionary.
    *The resulting dictionary is wrapped in a custom type `ContentJSON`.

    Args:
        filepath (str): Path to `.json` file.

    Returns:
        ContentJSON: `.json` file content.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file content is not valid JSON.
    """
    with open(file=filepath, mode='r') as json_file:
        file_content: Any = json.load(fp=json_file)

    content: ContentJSON = ContentJSON(file_content)

    return content
