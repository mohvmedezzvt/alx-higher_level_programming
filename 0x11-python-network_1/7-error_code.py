#!/usr/bin/python3
"""Takes in a URL,
Sends a request to the URL and
Displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.text)

    if r.status_code // 100 == 4:
        print(f"Error code: {r.status_code}")
