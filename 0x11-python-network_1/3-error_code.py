#!/usr/bin/python3
"""Takes in a URL,
Sends a request to the URL and
Displays the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
