#!/usr/bin/python3
"""A Module contains the to_json_string function.
"""
from json import dumps


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Args:
        my_obj (object): The object will return the JSON representation of it.

    Returns:
        str: The JSON representation of an object (string)
    """
    json_str = dumps(my_obj)
    return json_str
