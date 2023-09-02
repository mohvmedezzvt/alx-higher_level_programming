#!/usr/bin/python3

"""
Square Module

This module defines the `Square` class, which represents a square shape and
provides methods to manipulate and calculate its attributes.

Classes:
    Square:
        Represents a square with a size attribute.

Example usage:
>>> my_square = Square(5)
>>> print(my_square.area())
25
>>> my_square.size = 3
>>> print(my_square.area())
9
>>> my_square.size = "five"
Traceback (most recent call last):
    ...
TypeError: size must be an integer
"""


class Square:
    """
    Square class with a private instance attribute __size,
    getter, setter, and a method to calculate the area.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size attribute.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size
