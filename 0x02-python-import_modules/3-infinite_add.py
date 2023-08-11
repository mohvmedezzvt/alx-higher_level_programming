#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num_args = len(argv) - 1
    sum_args = 0
    if num_args > 0:
        for arg in argv[1:]:
            sum_args += int(arg)
        print(sum_args)
    else:
        print(0)
