#!/usr/bin/python3
"""Takes in a letter and
Sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    data = {'q': q}

    r = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        json_data = r.json()
        if json_data:
            print("[{}] {}".format(json_data.get('id'),
                                   json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
