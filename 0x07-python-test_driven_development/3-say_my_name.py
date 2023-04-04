#!/usr/bin/python3
"""
This module prints my full mane
"""
def say_my_name(first_name, last_name=""):
    '''
    This function returns the first and last name procceded by 'my name is...'
    Args:
        first_name: first name of the input
        last_name: last name of the input
    Returns:
        returns the the first and las name
    Raises:
        TypeError: first and las name must not be other than string
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    my_name_is = ("My name is {:s} {:s}".format(first_name, last_name))
    return print(my_name_is)
