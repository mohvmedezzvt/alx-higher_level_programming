#!/usr/bin/python3
"""A module that contains MyList Class.
"""


class MyList(list):
    """a class MyList that inherits from list

    Args:
        list (list): list to print
    """
    def print_sorted(self):
        """Print the list in ascending sorted order.
        """
        if self is None:
            print([])
        else:
            sorted_list = sorted(self)
            print(sorted_list)
