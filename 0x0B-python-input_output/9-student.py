#!/usr/bin/python3
""" Defines student class """


class Student():
    """ Student class """

    def __init__(self, first_name, last_name, age):
        """ Initialize public variables """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Return class dictionary """
        return self.__dict__
