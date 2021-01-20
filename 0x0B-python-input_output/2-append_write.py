#!/usr/bin/python3
""" Continues editing a file """


def append_write(filename="", text=""):
    """ Writes text in file """
    with open(filename, 'a', encoding='utf8') as file:
        return file.write(text)
