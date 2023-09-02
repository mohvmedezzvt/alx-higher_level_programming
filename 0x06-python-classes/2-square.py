#!/usr/bin/python3

"""
1-square Module

This module defines a basic square shape represented by the `Square` class.
It currently serves as a template for creating square objects.

Example usage:
>>> Square = __import__('0-square').Square
>>> my_square = Square(3)
>>> type(square)
<class '__main__.Square'>
"""


class Square:
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
