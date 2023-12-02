#!/usr/bin/python3
"""Takes in a letter and
Sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    data{'q': q}

    r = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        json_data = r.json()
        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
