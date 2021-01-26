#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter """
        return self.height

    @size.setter
    def size(self, size):
        """ Setter """
        self.height = size
        self.width = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.height)

    def to_dictionary(self):
        return "{'id': {}, 'x': {}, 'size': {}, 'y': {}}".format(self.id, self.x, self.height, self.y)
