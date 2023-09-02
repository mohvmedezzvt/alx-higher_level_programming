#!/usr/bin/python3

"""
Square Module

This module defines the `Square` class, which represents a square shape.
The class includes methods to calculate the area of the square.

Classes:
    Square:
        Represents a square with a given size.

Example usage:
>>> square1 = Square(5)
>>> square2 = Square()
>>> print(square1.area())
25
>>> print(square2.area())
0
"""


class Square:
    """
    Square Class

    This class defines a square and provides methods to calculate its area.
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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size
