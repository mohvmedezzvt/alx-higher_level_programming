#!/usr/bin/python3

"""
Square Module

This module defines the `Square` class, which represents a square shape and
provides methods to manipulate and calculate its attributes. The class includes
a private size attribute with getter and setter methods for controlling access
and ensuring proper validation.

Classes:
    Square:
        Represents a square with a size attribute.

Example usage:
>>> my_square = Square(3)
>>> print(my_square.area())
>>> my_square.my_print()
9
###
###
###
>>> my_square.size = 5
>>> print(my_square.area())
25
>>> my_square.size = "three"
Traceback (most recent call last):
    ...
TypeError: size must be an integer
"""


class Square:
    """
    This class represents a square and provides methods to manipulate and
    calculate its attributes.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer (in the setter method).
            ValueError: If size is less than 0 (in the setter method).
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

    def my_print(self):
        """
        prints in stdout the square with the character #.
        """
        size = self.__size

        if size == 0:
            print()
        else:
            for i in range(size):
                for j in range(size):
                    print("#", end="")
                print()
