#!/usr/bin/python3
import json
""" Define a base """


class Base():
    """ base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == []:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        file = cls.__name__ + ".json"
        with open(file, 'w') as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dic = [object.to_dictionary() for object in list_objs]
                jsonfile.write(Base.to_json_string(dic))
