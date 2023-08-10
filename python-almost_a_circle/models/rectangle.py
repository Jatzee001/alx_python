#!/usr/bin/python3

"""
Defines a rectangle class
"""

from models.base import Base

class Rectangle(Base):
    """
    Represent a rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__int__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    @property
    def width(self):
        """
        getter the width of the Rectangle.
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        setter the width of the Rectangle.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        getter the height of the Rectangle.
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        setter the height of the Rectangle.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        getter the x of the Rectangle.
        """
        return self.__x
    
    @x.setter
    def x(self, value):
        """
        setter the x of the Rectangle.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        getter the y of the Rectangle.
        """
        return self.__y
    
    @y.setter
    def y(self, value):
        """
        setter the y of the Rectangle.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        area docs
        """
        return self.__width * self.__height
    
    def display(self):
        """
        Print the Rectangle using '#' character.
        """
        for row in range(self.y):
            print()
        else:
            for row in range(self.height):
                for column in range(self.x):
                    print("#", end="")
                else:
                    for column in range(self.width):
                        print("#", end="")
                    else:
                        print()
        
    def __str__(self) -> str:
        """
        str update
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
    
    def update(self, *args, **kwargs):
        """
        update attributes
        """
        args_lenght = len(args)
        kwargs_length = len(kwargs)

        for key, value in kwargs.items():
            if key =="id":
                self.id= value
            elif key == "width":
                self.width = value
            elif key == "height":
                self.height = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value

        if args_lenght > 0:
            self.id = args[0]
        if args_lenght > 1:
            self.width = args[1]
        if args_lenght > 2:
            self.height = args[2]
        if args_lenght > 3:
            self.x = args[3]
        if args_lenght > 4:
            self.y = args[4]