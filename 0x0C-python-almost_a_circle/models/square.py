#!/usr/bin/python3
""" Define a square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor class """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ Getter"""
        return self.__size

    @size.setter
    def size(self, size):
        """ Setter """
        self.height = size
        self.width = size
