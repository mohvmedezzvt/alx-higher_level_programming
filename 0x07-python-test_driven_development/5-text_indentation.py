#!/usr/bin/python3
"""This module provides a function for adding extra newlines
after specific characters.
"""


def text_indentation(text):
    """Adds two newlines after each '.', '?', or ':'
    character in the given text.

    Args:
        text (str): The input text to process.

    Raises:
        TypeError: If the input text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    lines = text.splitlines()

    for line in lines:
        line = line.strip()
        if line:
            for c in line:
                print(c, end="")
                if c in special_chars:
                    print("\n")
