#!/usr/bin/python3
"""This module defines a basic Rectangle class.
"""


class Rectangle:
    """A class Rectangle that defines a rectangle.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height.

        Args:
            width (int, optional): The width of the Rectangle. Defaults to 0.
            height (int, optional): The height of the Rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculate the rectangle Area.

        Returns:
            int: Rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the rectangle perimeter.

        Returns:
            int: Rectangle perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: The string representing the rectangle
            using the '#' characters.
        """
        if self.__height == 0 or self.__width == 0:
            return ""

        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"

        return rectangle_str[:-1]

    def __repr__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: A string representation of the object.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Destructor method to print a message when an instance is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
