#!/usr/bin/python3
"""inherited from the rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square which inherite rectangle class"""

    def __init__(self, size):
        """initializing the arguments"""
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns the area of the rectangle"""
        return self.__size * self.__size

    def __str__(self):
        """prints the sting of the class"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
