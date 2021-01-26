#!/usr/bin/python3
""" define a rectangle """
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """" Getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ Getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x <= 0:
            raise ValueError("x must be > 0")
        self.__x = x

    @property
    def y(self):
        """ Getter"""
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            """ Setter """
            raise TypeError("y must be an int")
        if y <= 0:
            raise ValueError("y must be > 0")
        self.__y = y

    def area(self):
        """ Returns the area of a rectangle """
        return self.__height * self.__width

    def display(self):
        """ prints the rectangle instance with # """
        for y in range(self.__y):
            print()
        for height in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for width in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ Returns the details of the rectangle """
        return  "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}" . format (self.id, self.__x, self.__y, self.__width , self.__height) 

    def to_dictionary(self):
        """ Rectangle dictionary """
        return "{'x': {}, 'y': {}, 'id':{}, 'height': {}, 'width': {}}".format(self.__x, self.__y, self.id, self.__height, self.__width)
