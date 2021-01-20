#!/usr/bin/python3
""" Append a text after a word is found """


def append_after(filename="", search_string="", new_string=""):
    """ Append text """
    buff = ""
    with open(filename) as read_file:
        for line in read_file:
            buff += line
            if search_string in line:
                buff += new_string
    with open(filename, 'w') as write_file:
        write_file.write(buff)
