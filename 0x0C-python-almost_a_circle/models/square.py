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
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        dic_ob = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return dic_ob
