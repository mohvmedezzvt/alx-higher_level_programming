#!/usr/bin/python3
"""A Module contains the write_file function.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8).

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        written = file.write(text)

    return written
