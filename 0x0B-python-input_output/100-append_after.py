#!/usr/bin/python3
"""module which addis a line of text"""


def append_after(filename="", search_string="", new_string=""):
    """the function which appends after the existing one """
    with open(filename, 'r') as file:
        lines = file.readlines()
        """reads and gets the existing string"""

    with open(filename, 'w') as file:
        """writes the new string"""
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
