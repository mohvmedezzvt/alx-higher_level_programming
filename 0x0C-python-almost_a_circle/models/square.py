#!/usr/bin/python3
"""A module contains the Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class representing a square.

    Args:
        Rectangle (class): The Parent Class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square in pixels.
            x (int, optional): The x-coordinate of the square's position
            (default is 0).
            y (int, optional): The y-coordinate of the square's position
            (default is 0).
            id (int, optional): The identifier of the square
            (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Updates attributes based on the given arguments.

        Args:
            *args: Arguments in the order: id, width, height, x, y.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)
