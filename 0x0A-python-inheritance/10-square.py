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
