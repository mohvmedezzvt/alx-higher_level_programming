#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    biggest = int(my_list[0])
    for i in range(len(my_list) - 1):
        if biggest < int(my_list[i + 1]):
            biggest = my_list[i + 1]

    return biggest
