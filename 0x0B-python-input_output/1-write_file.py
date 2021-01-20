#!/usr/bin/python3
""" writes in a file """


def write_file(filename="", text=""):
    """ Writes text in file """
    with open(filename, 'w', encoding='utf8') as file:
        return file.write(text)
