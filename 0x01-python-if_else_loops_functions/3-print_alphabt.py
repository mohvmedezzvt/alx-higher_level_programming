#!/usr/bin/python3
for letter in range(97, 123):
    if letter == 101 or letter == 113:
        continue
    else:
        print(f"{letter:c}".format(letter), end="")
