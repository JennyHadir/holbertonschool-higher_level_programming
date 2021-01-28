#!/usr/bin/python3
""" Define a base class"""
import json


class Base():
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Base constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the json string representation """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Returns a list of a json representation """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Write json rep to a file """
        file = cls.__name__ + ".json"
        with open(file, 'w', encoding="UTF-8") as jsfile:
            if list_objs is None:
                list_objs = []
            dic = [i.to_dictionary() for i in list_objs]
            jsfile.write(cls.to_json_string(dic))

    @classmethod
    def create(cls, **dictionary):
        """ Return an instances """
        if cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        else:
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Return a file containt a json list """
        file = cls.__name__ + ".json"
        try:
            with open(file, 'r', encoding="UTF-8") as jsonfile:
                dic = Base.from_json_string(jsonfile.read())
                return(cls.create(**item) for item in dic)
        except IOError:
            return []
