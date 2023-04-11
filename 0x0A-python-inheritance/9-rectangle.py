#!/usr/bin/python3
"""module basegeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this class represents a rectangle using BaseGeometry"""

    def __init__(self, width=0, height=0):
        """Intialize a new rectangle"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Prints the rectangle string"""
        return "[Rectangle] {}/{}" .format(self.__width, self.__height)
