#!/usr/bin/python3
"""
This module has an addition function of the two integers or floats
"""


def add_integer(a, b=98):
    """"
    returns the sum of two integers or floats as sum of integer
    Args:
        a: is the first number and
        b: is the second number
    Return:
        the sum of them
    Raises:
        TypeError: if one of the argument is not int or float
        TYpeError: if one of the arguments are non numbers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    """changing the float argument to integer"""
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
    """returns the sum of the arguments"""
    return a + b
