#!/usr/bin/python3
""" Takes in a URL,
Sends a request to the URL and
Displays the value of the variable X-Request-Id in the response header
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    x_request_id = r.headers.get('X-Request-Id')

    if x_request_id:
        print(x_request_id)
