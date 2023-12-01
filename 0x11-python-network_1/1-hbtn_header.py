#!/usr/bin/python3
"""Takes in a URL,
Sends a request to the URL and
Displays the value of the X-Request-Id variable found
in the header of the response.
"""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    x_request_id = response.getheader('X-Request-Id')

    if x_request_id:
        print(x_request_id)
