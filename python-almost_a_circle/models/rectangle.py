# In the file models/rectangle.py
from models.base import Base # Import the Base class

class Rectangle(Base): # Class Rectangle inherits from Base
    # Private instance attributes, each with its own public getter and setter
    def _init_(self, width, height, x=0, y=0, id=None): # Class constructor
        super()._init_(id) # Call the super class with id
        self.width = width # Assign each argument to the right attribute
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self): # Getter for __width
        return self.__width

    @width.setter
    def width(self, value): # Setter for __width
        if type(value) is not int: # Validate the value
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value # Assign the value to the private attribute

    @property
    def height(self): # Getter for __height
        return self.__height

    @height.setter
    def height(self, value): # Setter for __height
        if type(value) is not int: # Validate the value
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value # Assign the value to the private attribute

    @property
    def x(self): # Getter for __x
        return self.__x

    @x.setter
    def x(self, value): # Setter for __x
        if type(value) is not int: # Validate the value
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value # Assign the value to the private attribute

    @property
    def y(self): # Getter for __y
        return self.__y

    @y.setter
    def y(self, value): # Setter for __y
        if type(value) is not int: # Validate the value
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value # Assign the value to the private attribute