#!/usr/bin/python3
""" Class Base Geometry """


class BaseGeometry():
    """ Error if area is not defined """
    def area(self):
        raise Exception("area() is not implemented")

    """ Check positive number"""
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
