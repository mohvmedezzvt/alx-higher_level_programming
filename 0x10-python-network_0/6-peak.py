#!/usr/bin/python3
"""a module that defines the find_peak function.
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None

    list_of_integers = sorted(list_of_integers)
    return list_of_integers[-1]
