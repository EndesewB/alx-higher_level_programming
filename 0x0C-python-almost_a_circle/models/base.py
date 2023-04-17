#!/usr/bin/python3
"""This is the base class module"""


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
