#!/usr/bin/python3
"""module to create object from json"""
import json


def load_from_json_file(filename):
    """ a function that writes an Object from json"""
    with open(filename, 'r') as file:
        string_json = file.read()
        return json.loads(string_json)
