#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set()
    for i in my_list:
        my_set.add(i)

    total_sum = 0
    for i in my_set:
        total_sum += i

    return total_sum
