#!/usr/bin/python3
""" list 10 commits (from the most recent to oldest)
 of the repository “rails” by the user “rails” """
from sys import argv
import requests
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    commits = r.json()
    for commit in commits[:10]:
        print("{}: {}"
              .format(commit.get('sha'),
                      commit.get('commit').get('author').get('name')))
