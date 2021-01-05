#!/usr/bin/python3
""" Square class """


class Square:
    """ Square instances """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """ Computes square area """
    def area(self):
        res = self.__size * self.__size
        return res

    """ Computes square size """
    @property
    def size(self):
        return self.__size

    """ Sets square size """
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ Prints all """
    def my_print(self):
        if self.__size > 0:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")

    """ Define position property """
    @property
    def position(self):
        return self.__position

    """ Sets position """
    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value