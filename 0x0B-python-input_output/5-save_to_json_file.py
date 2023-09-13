#!/usr/bin/python3
"""A Module contains the to_json_string function.
"""
from json import dumps


def save_to_json_file(my_obj, filename):
    json_str = dumps(my_obj)

    with open(filename, 'w', encoding='utf-8') as file:
        num = file.write(json_str)

    return num
