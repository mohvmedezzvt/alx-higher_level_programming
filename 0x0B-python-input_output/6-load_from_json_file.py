#!/usr/bin/python3
"""A Module contains the load_from_json_file function.
"""
from json import load


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”.

    Args:
        filename (str): The JSON file

    Returns:
        object: The object loaded from filename
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return load(file)
