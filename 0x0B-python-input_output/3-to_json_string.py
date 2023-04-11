#!/usr/bin/python3
"""The method to change to json string"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object as a string."""
    return json.dumps(my_obj)
