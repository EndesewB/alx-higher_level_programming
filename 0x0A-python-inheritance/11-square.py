#!/usr/bin/python3
"""
Module for the `Square` class that inherits from `Rectangle`.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square that inherits from `Rectangle`.
    """
    def __init__(self, size):
        """
        Initializes an instance of the `Square` class.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the `Square` class.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        Calculates and returns the area of the `Square` instance.
        """
        return self.__size ** 2
