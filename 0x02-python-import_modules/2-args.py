#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) - 1 > 0:
        print("{:d} {}:".format(len(argv) - 1, "argument" if len(argv) - 1 == 1 else "arguments"))

        for arg in range(len(argv) - 1):
            print("{:d}: {}".format(arg + 1, argv[arg + 1]))
    else:
        print("0 arguments.")
