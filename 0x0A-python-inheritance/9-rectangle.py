#!/usr/bin/python3
"""a Module that contains Rectangle Class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Class Rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        """Return a string representation of the Rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Calculate the area of the Rectangle.

        Returns:
            int: The area of the Rectangle.
        """
        return self.__width * self.__height
