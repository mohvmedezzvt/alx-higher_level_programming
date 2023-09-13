#!/usr/bin/python3
"""A Module contains the to_json_string function.
"""
from json import dump


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (object): The object will be written the JSON
        representation of it.
        filename (str): The file will be written to it the JSON representation.

    Returns:
        int: The number of bytes written to filename
    """
    with open(filename, 'w', encoding='utf-8') as file:
        dump(my_obj, file)
