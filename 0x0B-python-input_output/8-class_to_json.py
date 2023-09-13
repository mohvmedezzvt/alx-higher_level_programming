#!/usr/bin/python3
"""A Module conatins class_to_json function.
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.

    Args:
        obj (object): The object to returns it's dictionary description.

    Returns:
        dict: The dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.
    """
    return obj.__dict__
