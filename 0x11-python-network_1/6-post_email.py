#!/usr/bin/python3
""" Takes in a URL and an email,
 sends a POST request to the passed URL with the email as a parameter,
 and displays the body of the response """
if __name__ == "__main__":
    import requests
    from sys import argv
    payload = {'email': argv[2]}
    url = argv[1]
    r = requests.post(url, data=payload)
    print(r.text)
