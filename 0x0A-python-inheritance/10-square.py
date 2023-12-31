#!/usr/bin/python3
"""a Module that contain the Square class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Class Square that inherits from Rectangle.

    Args:
        Rectangle (_type_): _description_
    """

    def __init__(self, size):
        """Initialize a Square instance with size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
