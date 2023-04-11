#!/usr/bin/python3
"""The module which opens a file"""


def read_file(filename=""):
    """the method which reads file to stdout"""

    with open(filename, 'r', encoding="utf-8") as file:
        contents = file.read()
        print(contents)
