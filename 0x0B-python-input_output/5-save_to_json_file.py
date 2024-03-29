#!/usr/bin/python3
"""module to write as the form of json"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w') as file:
        return json.dump(my_obj, file)
