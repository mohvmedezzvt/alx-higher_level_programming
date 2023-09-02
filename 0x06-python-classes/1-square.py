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
    """
    Square class with a private instance attribute __size.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
