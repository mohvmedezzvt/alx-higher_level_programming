#!/usr/bin/python3
"""a Module that contains BaseGeometry Class.
"""


class BaseGeometry():
    """A Class BaseGeometry.
    """
    def area(self):
        """Raise an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value:
        - If value is not an integer, raise a TypeError exception with
        the message "<name> must be an integer".
        - If value is less than or equal to 0, raise a ValueError exception
        with the message "<name> must be greater than 0".

        Args:
            name (string): A string representing the name of the value.
            value (int): The value to be validated.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
