#!/usr/bin/python3
"""
This module provides a function for adding two integers or floats.

It includes additional details about the module's purpose and usage.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
