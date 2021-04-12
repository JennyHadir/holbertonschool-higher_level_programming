#!/usr/bin/python3
""" takes in a letter and sends a POST request
 to http://0.0.0.0:5000/search_user with the letter as a parameter. """
from sys import argv
import requests
if __name__ == "__main__":
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', {'q': q})
    try:
        r_dict = r.json()
        id = r_dict.get('id')
        name = r_dict.get('name')
        if len(r_dict) == 0 or id is None or name is None:
            print("No result")
        else:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
    except Exception:
        print("Not a valid JSON")
