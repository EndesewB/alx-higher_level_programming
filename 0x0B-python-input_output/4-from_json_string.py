#!/usr/bin/python3
"""module from the json to object"""
import json


def from_json_string(my_str):
    """a function that returns an object represented by a JSON string"""
    return json.loads(my_str)
