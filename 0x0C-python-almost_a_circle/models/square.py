#!/usr/bin/python3
"""Square module attribute inherited from Base and Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The square class that inherits the rectangle class attributes"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        """getting and setting the size attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def area(self):
        """returns the area of the square"""
        return self.size ** 2

    def __str__(self):
        """string formating of the square"""
        w = f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
        return w

    def display(self):
        """displays the representation of square"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """using args and kwargs to update arguments"""
        if args:
            self.id = args[0]
        elif len(args) > 1:
            self.width = args[1]
        elif len(args) > 2:
            self.height = args[2]
        elif len(args) > 3:
            self.x = args[3]
        elif len(args) > 4:
            self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
