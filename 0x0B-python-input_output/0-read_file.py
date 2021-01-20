#!/usr/bin/python3
""" Open a file from UTF-8 """


def read_file(filename=""):
    """ Prints a file """
    with open(filename, encoding='utf8') as file:
        for line in file:
            print(line, end="")
