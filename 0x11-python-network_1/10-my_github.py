#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and
Uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    auth = (sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)

    try:
        r.raise_for_status()
        json_data = r.json()
        print(json_data.get('id', 'None'))
    except requests.exceptions.HTTPError as e:
        print("None")
