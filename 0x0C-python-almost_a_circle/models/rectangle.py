#!/usr/bin/python3
""" Define a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter """
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
        """ Getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ Getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Return the area of rectangle """
        return self.__height * self.width

    def display(self):
        """ Prints a rectangle with # """
        for y in range(self.__y):
            print()
        for height in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for width in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ Return details about rectangle """
        re = "[Rectangle] ({}) {}/{} ".format(self.id, self.__x, self.__y)
        return re + "- {}/{}".format(self.__width, self.__height)

    def update(self, *args):
        """ Assigns an argument to each attribute """
        if len(args):
            i = 1
            for value in args:
                if i == 1:
                    self.id = value
                if i == 2:
                    self.__width = value
                if i == 3:
                    self.__height = value
                if i == 4:
                    self.__x = value
                if i == 5:
                    self.__y = value
                i += 1
