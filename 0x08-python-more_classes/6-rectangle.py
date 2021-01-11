#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ Rectangle define """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        rect = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.height):
                for j in range(self.__width):
                    rect += '#'
                if (i < self.__height - 1):
                    rect += '\n'
        return rect

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
