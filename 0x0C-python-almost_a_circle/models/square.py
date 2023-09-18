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

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
