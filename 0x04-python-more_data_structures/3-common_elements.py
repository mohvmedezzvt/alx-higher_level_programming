#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_3 = set(set_1 & set_2)  # or set_3 = set_1.intersection(set2)
    return set_3
