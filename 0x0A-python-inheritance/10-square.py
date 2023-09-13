#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""a Module that contain the Square class.
"""


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
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the Square.
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
