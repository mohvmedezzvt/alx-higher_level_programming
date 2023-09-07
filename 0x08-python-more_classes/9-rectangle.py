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
        self.__print_symbol = "#"
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
            rectangle_str += str(self.print_symbol) * self.__width + "\n"

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

    @property
    def print_symbol(self):
        """The print_symbol getter.

        Returns:
            Any: The symbol used for string representation.
        """
        return self.__print_symbol

    @print_symbol.setter
    def print_symbol(self, value):
        """The print_symbol setter.

        Args:
            value (Any): The symbol to be used for string representation.
        """
        self.__print_symbol = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to find the bigger or equal rectangle based on area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: The bigger or equal rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method to create a new Rectangle instance as a square.

        Args:
            cls (class): The class itself (Rectangle).
            size (int): The size of the square. Defaults to 0.

        Returns:
            Rectangle: A new Rectangle instance with width == height == size.
        """
        return cls(size, size)
