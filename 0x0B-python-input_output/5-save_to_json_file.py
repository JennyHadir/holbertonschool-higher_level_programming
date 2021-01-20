#!/usr/bin/python3
""" Saves into json """
import json


def save_to_json_file(my_obj, filename):
    """ Saves json in file """
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
