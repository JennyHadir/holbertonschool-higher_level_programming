#!/usr/bin/python3
""" Define Square class"""


class Square:
    """ Square instances """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """ Computes square area """
    def area(self):
        res = self.__size * self.__size
        return res

    """ Define size property """
    @property
    def size(self):
        return self.__size

    """ Define Square size """
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ Prints square size """
    def my_print(self):
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
