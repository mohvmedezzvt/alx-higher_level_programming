#!/usr/bin/python3
"""A module contains the Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """A class representing a rectangle.

    Args:
        Base (class): The Parent Class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position
            (default is 0).
            y (int, optional): The y-coordinate of the rectangle's position
            (default is 0).
            id (int, optional): The identifier of the rectangle
        (default is None).
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        self.__height = value
