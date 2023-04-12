#!/usr/bin/python3
"""The student class module"""


class Student:
    """my class student"""
    def __init__(self, first_name, last_name, age):
        """initializing attribute of the class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dict of the class student if the attribute is existed"""
        if attrs is None:
            return self.__dict__
        else:
            json_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
            return json_dict

    def reload_from_json(self, json):
        """loading attribute from the file"""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
