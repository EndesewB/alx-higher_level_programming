#!/usr/bin/python3
"""module basegeometry"""


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
        if type(value) != int:
            raise TypeError(f" {name} must be an integer".format(value))
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0".format(value))
