#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for val in list(a_dictionary.keys()):
        if a_dictionary[val] == value:
            del a_dictionary[val]
    return a_dictionary
