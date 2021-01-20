#!/usr/bin/python3
""" Creates an object from json """
import json


def load_from_json_file(filename):
    """ Returns json from file """
    with open(filename, encoding='utf-8') as file:
        return json.loads(file.read())
