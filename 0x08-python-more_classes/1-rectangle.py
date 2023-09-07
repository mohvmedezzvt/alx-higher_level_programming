#!/usr/bin/python3
"""This module defines a basic Rectangle class.
"""


class Rectangle:
    """A class Rectangle that defines a rectangle.
    """

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height.

        Args:
            width (int, optional): The width of the Rectangle. Defaults to 0.
            height (int, optional): The height of the Rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """The width getter.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """The width setter.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: When the value is not integer.
            ValueError: When the value is smaller than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """The height getter.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """The height setter.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: When the value is not integer.
            ValueError: When the value is smaller than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
