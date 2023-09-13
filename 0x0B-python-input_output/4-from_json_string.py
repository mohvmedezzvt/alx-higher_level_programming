#!/usr/bin/python3
"""A Module contains the to_json_string function.
"""
from json import loads


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to return it's object representation.

    Returns:
        obj: The object (Pyhton data structure) represented by a JSON string.
    """
    return loads(my_str)
