#!/usr/bin/python3
"""The student class module"""


class Student:
    """my class student"""
    def __init__(self, first_name, last_name, age):
        """initializing attribute of the class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dict of the class student"""
        return self.__dict__
