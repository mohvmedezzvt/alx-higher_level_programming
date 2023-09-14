#!/usr/bin/python3
"""A Module
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text into a file after each line
    containing a specific string.

    Args:
        filename (str, optional): The name of the file to modify.
        Defaults to "".
        search_string (str, optional): The string to search for in each line of
        the file. Defaults to "".
        new_string (str, optional): The line of text to insert after each
        occurrence of search_string. Defaults to "".
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(filename, 'a', encoding='utf-8') as file:
            for line in lines:
                file.write(line)
                if search_string in line:
                    file.write(new_string)
    except FileNotFoundError:
        pass
