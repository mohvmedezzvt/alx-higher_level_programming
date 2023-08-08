#!/usr/bin/python3
for index1 in range(10):
    for index2 in range(index1 + 1, 10):
        if index1 == 8 and index2 == 9:
            print("{:d}{:d}".format(index1, index2))
        else:
            print("{:d}{:d}, ".format(index1, index2), end="")
