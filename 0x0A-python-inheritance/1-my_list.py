#!/usr/bin/python3
""" inherit from list """


class MyList(list):
    """ inherit from list """
    def print_sorted(self):
        """ Print sorted list """
        print(sorted(self))
