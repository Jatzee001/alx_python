#!/usr/bin/python3

"""Defines a rectangle class"""
from models.base import Base

class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, id=None):
        """Initialize a new Rectangle.

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
        super().__init__(id)
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
        elif x <= 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y <= 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = y

    @property
    def width(self):
        """
        get function for the width private instance attribute.
        """
        return self.__width
    
    @width.setter
    def width(self, width):
        """
        set function for the width private instance attribute.
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """
        get function for the height private instance attribute.
        """
        return self.__height
    
    @height.setter
    def height(self, height):
        """
        set function for the height private instance attribute.
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """
        get function for the x private instance attribute.
        """
        return self.__x
    
    @x.setter
    def x(self, x):
        """
        set function for the x private instance attribute.
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x <= 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = x

    @property
    def y(self):
        """
        get function for the y private instance attribute.
        """
        return self.__y
    
    @y.setter
    def y(self, height):
        """
        set function for the y private instance attribute.
        """
        if type(height) is not int:
            raise TypeError("y must be an integer")
        elif y <= 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = y

    def area(self):
        """
        Return the area of the rectangle
        """
        return self.__width * self.__height
    
    def display(self):
        """
        Rectangle display public method
        """
        for row in range(self.__y):
            print()
        else:
            for row in range(self.height):
                for column in range(self.__x):
                    print(" ", end="")
                else:
                    for column in range(self.__width):
                        print("#", end="")
                    else:
                        print()

    def __str__(self):
        """
        rewrite default str method string
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update the Rectangle
        Args:
            *args (ints): New attribute values.
                -1st argument represents id attribute
                -2nd argument represents width attribute
                -3rd argument reprents height attribute
                -4th argument reprents x attribute
                -5th argument reprents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        args_length = len(args)
        if args_length > 0:
            self.id = args[0]
        if args_length > 1:
            self.__width = args[1]
        if args_length > 2:
            self.__height = args[2]
        if args_length > 3:
            self.__x = args[3]
        if args_length > 4:
            self.y = args[4]

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
    
    