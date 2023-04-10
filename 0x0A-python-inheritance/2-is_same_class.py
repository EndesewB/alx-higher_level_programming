#!/usr/bin/python3
"""module which compare its instance and type"""


def is_same_class(obj, a_class):
    """a mothod which compares its object is instance of the same class
    Args:
        obj:
        object that to be commpared
        a_class:
        instance of the class
    Returns:
        boolean
        """
    return(type(obj)) is a_class
