#!/usr/bin/python3
"""Class Square inherits from rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square inherits from rectangle class"""
    def __init__(self, size):
        """New rectangle"""
        if self.integer_validator("size", size):
            self.__size = size
        super().__init__(size, size)
