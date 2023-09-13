#!/usr/bin/python3
"""A Module the contains the read_file function.
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str, optional): The file to read from. Defaults to "".
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
        print(data.strip())
