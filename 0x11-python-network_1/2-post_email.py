#!/usr/bin/python3
""" Takes in a URL and an email,
 sends a POST request to the passed URL with the email as a parameter,
 and display the body of the response (decoded in utf-8) """
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv
    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as reponse:
        print(reponse.read().decode('utf-8'))
