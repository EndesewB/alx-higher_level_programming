#!/usr/bin/python3
"""
The rectangle class module
"""


class Rectangle:
    """
    This is the rectangle class
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
    '''
    This class sets the rectangle height and width
    Args:
        width: The first dimension of the rectangle
        height: the height of the rectangle
    Returns: the width and height of the rectangle will be returned
    '''
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value
    '''
    rectangle width setter
    '''

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
    '''
    rectangle height setter
    '''
