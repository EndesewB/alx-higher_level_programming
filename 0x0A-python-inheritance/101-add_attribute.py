#!/usr/bin/python3
"""a method  to add attribute ot the object"""


def add_attribute(obj, name, value):
    """
    Add a new attribute to an object if it's possible.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value
