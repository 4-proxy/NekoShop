# -*- coding: utf-8 -*-

"""
description

Copyright 2024 4-proxy
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = ["get_content_from_json", "ContentJSON"]

__author__ = "4-proxy"
__version__ = "0.1.0"

import json

from typing import Any, Dict


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ContentJSON(Dict[str, Dict[str, Any]]):
    pass


# -----------------------------------------------------------------------------
def get_content_from_json(filepath: str) -> ContentJSON:
    with open(file=filepath, mode='r') as json_file:
        file_content: Any = json.load(fp=json_file)

    content: ContentJSON = ContentJSON(file_content)

    return content
