#!/usr/bin/python3
"""Inheris from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Instantiates a Rectangle object with the given width and height.
        Args:
            width: The width of the rectangle. Must be a positive integer.
            height: The height of the rectangle. Must be a positive integer.
        Returns: width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
