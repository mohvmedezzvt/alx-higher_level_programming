#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name(" MOHmed", "ezZat   ")
say_my_name("Walter", "White")
say_my_name("bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
