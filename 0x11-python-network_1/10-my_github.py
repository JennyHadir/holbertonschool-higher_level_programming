#!/usr/bin/python3
""" Takes your GitHub credentials (username and password)
 and uses the GitHub API to display your id"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth
r = requests.get("https://api.github.com/repos/{}".format(argv[1],
                 auth=HTTPBasicAuth(argv[1], argv[2])))
print(r.json().get('id'))
