#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = set(set_1 ^ set_2)  # or set_3 = set1.symmetric_difference(set_2)
    return set_3
