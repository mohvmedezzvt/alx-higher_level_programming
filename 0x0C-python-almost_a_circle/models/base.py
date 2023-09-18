#!/usr/bin/python3
"""A module contains the Base Class.
"""
import json


class Base():
    """The Base Class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base Instance.

        Args:
            id (int, optional): The id. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
