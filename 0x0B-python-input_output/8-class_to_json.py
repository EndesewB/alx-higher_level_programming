#!/usr/bin/python3
"""the module which returns dict of the objects"""


def class_to_json(obj):
    """ returns the dictionary description with simple data structure"""
    return obj.__dict__
