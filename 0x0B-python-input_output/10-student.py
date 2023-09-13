#!/usr/bin/python3
"""A Module contains a class Student.
"""


class Student():
    """A class Student that defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance.

        Args:
            first_name (str): The Student first_name.
            last_name (str): The Student second_name.
            age (int): The Student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary representation of a Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            valid_attrs = {}
            for attr in attrs:
                if hasattr(self, attr):
                    valid_attrs[attr] = getattr(self, attr)
            return valid_attrs
