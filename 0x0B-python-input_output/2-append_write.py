#!/usr/bin/python3
"""The module to write and append to the file"""


def append_write(filename="", text=""):
    """this method appends the text and prints length of the string/text"""
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(text)
        return len(text)
