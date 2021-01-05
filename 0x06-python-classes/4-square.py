#!/usr/bin/python3
""" Square class """


class Square:
    """ Define Square """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """ Define Square area """
    def area(self):
        res = self.__size * self.__size
        return res

    """ Define size property """
    @property
    def size(self):
        return self.__size

    """ Define size again?"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
