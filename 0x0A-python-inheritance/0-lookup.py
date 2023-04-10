#!/usr/bin/python3
"""The module to return all available atribute of the object"""


def lookup(obj):
    """the lookup method to display the atribute of onject
    Args:
        obj: object that contains attributes
    Returns:
        attributes
        """


    return dir(obj)
""" dir is the built-in function that returns the attributes"""
