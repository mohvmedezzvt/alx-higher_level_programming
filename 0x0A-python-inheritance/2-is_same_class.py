#!/usr/bin/python3
"""a Module contains is_same_class Class.
"""


def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is exactly an instance of the specified class;
        otherwise, False.
    """
    return type(obj) is a_class
