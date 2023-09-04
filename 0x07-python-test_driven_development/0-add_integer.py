#!/usr/bin/python3
"""
This module provides a function for adding two integers or floats.

It includes additional details about the module's purpose and usage.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats.
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
