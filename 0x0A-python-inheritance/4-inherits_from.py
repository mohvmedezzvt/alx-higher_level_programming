#!/usr/bin/python3
"""a Module that contains inherits_from function.
"""


def inherits_from(obj, a_class):
    """Check if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of
        a subclass (directly or indirectly) of the specified class;
        otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
