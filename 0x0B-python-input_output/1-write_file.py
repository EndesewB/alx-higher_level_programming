#!/usr/bin/python3
"""The module to write to the file"""


def write_file(filename="", text=""):
    """this method prints or returns the length of the string/text"""
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
        return len(text)
