#!/usr/bin/python3
""" Takes your GitHub credentials (username and password)
 and uses the GitHub API to display your id"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get('https://api.github.com/user',
                     auth=(argv[1], argv[2]))
    try:
        print(r.json().get['id'])
    except Exception:
        print('None')
