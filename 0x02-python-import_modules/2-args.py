#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num_args = len(argv) - 1
    args_word = "argument" if num_args == 1 else "arguments"

    if num_args > 0:
        print("{:d} {}:".format(num_args, args_word))

        for arg in range(len(argv) - 1):
            print("{:d}: {}".format(arg + 1, argv[arg + 1]))
    else:
        print("0 arguments.")
