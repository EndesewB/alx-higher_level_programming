#!/usr/bin/python3
"""The class that inherites the list class"""


class MyList(list):
    """This class inherites the atrributes of the builtin class 'list'
    Args:
        list: to be inherited built-in class
    Returns:
        inherited attributes and methods
        """

    def print_sorted(self):
        """The method which prints and sorts the list"""
        sortedList = sorted(self)
        print(sortedList)
