#!/usr/bin/python3
"""module basegeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class BaseGeometry:
    """This is an empty class basegeometry"""
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Public instance method that validates the value
        Args:
            name: A string representing the name of the value.
            value: The value to be validated.
        raises: TypeError: If the value is not an integer.
               ValueError: If the value is less or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f" {name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
class Rectangle(BaseGeometry):
    def __init__(self, width=0, height=0):
        """
        Instantiates a Rectangle object with the given width and height.
        Args:
            width: The width of the rectangle. Must be a positive integer.
            height: The height of the rectangle. Must be a positive integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
