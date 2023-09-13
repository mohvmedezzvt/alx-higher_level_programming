#!/usr/bin/python3
"""A Module contains the append_write function.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8).

    Args:
        filename (str, optional): The name of file to append to.
        Defaults to "".
        text (str, optional): The text to append to the filename.
        Defaults to "".

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num = file.write(text)

    return num
