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
        return self.width

    @size.setter
    def size(self, size):
        """ Setter """
        self.width = size
        self.height = size

    def __str__(self):
        sq = "[Square] ({}) {}/{}".format(self.id, self.x, self.y)
        return sq + " - {}".format(self.size)

    def update(self, *args, **kwargs):
        """ Assigns a key/value argument to each attribute """
        if len(args):
            i = 1
            for value in args:
                if i == 1:
                    self.id = value
                if i == 2:
                    self.size = value
                if i == 3:
                    self.x = value
                if i == 4:
                    self.y = value
                i += 1
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ Dictionary of rectangle """
        dic = {}
        dic["id"] = self.id
        dic["x"] = self.x
        dic["size"] = self.size
        dic["y"] = self.y
        return dic
