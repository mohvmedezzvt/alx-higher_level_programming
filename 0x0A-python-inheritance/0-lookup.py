#!/usr/bin/python3
"""A module contains a function that:
    Gets a list of available attributes and methods of an object.
"""


def lookup(obj):
    """Get a list of available attributes and methods of an object.

    Args:
        obj (obj): The object for which you want to retrieve
        attributes and methods.

    Returns:
        list: A list of strings containing the names of attributes and
        methods associated with the object.
    """
    return (dir(obj))
