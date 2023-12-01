#!/usr/bin/python3
"""Takes in a URL and an email address,
Sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    data = {'email': email}
    r = requests.post(sys.argv[1], data=data)

    print(f"Your email is: {email}")
