#!/usr/bin/python3
"""A module contains the Base Class.
"""


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
