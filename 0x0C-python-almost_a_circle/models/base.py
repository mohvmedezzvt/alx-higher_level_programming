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
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        if list_objs is None:
            list_objs = []

        file_name = cls.__name__ + ".json"
        json_list = [obj.to_dictionary() for obj in list_objs]

        with open(file_name, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create and return an instance with attributes set from a dict."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None

        dummy.update(**dictionary)
        return dummy
