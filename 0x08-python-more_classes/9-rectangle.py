#!/usr/bin/python3
"""
The rectangle class module
"""


class Rectangle:
    """
    This is the rectangle class
    """
    print_symbol = '#'  # print symbol of the rectangle
    number_of_instances = 0  # instance counter

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    '''
    This class sets the rectangle height and width
    Args:
        width: The first dimension of the rectangle
        height: the height of the rectangle
    Returns: the width and height of the rectangle will be returned
    '''

    @classmethod
    def square(cls, size=0):
        """Class method Square which takes the size of the rectangle
         and returns the area of the square
         Args:
             size: the size of the square
        Returns: the area
         """
        return cls(size, size)

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

    def area(self):
        return self.__width * self.__height

    '''
    Returns: the area of the rectangle
    '''

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    '''
    Returns: the perimeter of the rectangle
    '''

    def __str__(self):
        """Prints the rectangle representing symbols"""
        if self.width == 0 or self.height == 0:
            return ""
        rect_str = ""
        for i in range(self.height):
            for j in range(self.width):
                rect_str += str(self.print_symbol)
            if i != self.height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """Returns the representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Remaining instances after deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static methods which returns the biggest rectangle from the two"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
