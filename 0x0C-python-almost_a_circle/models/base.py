#!/usr/bin/python3
"""This is the base class module"""
import json


class Base:
    """Base class with private attributes managing criteria"""
    __nb_objects = 0
    """private object counter"""
    def __init__(self, id=None):
        """if id is passed, it will be setted id attribute"""
        """if it is not passed it will generate a unique id attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json representation of dicts"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json file to file objects"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            js_str = cls.to_json_string([ob.to_dictionary() for ob in list_objs])
            file.write(json_str)
