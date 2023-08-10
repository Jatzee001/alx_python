"""
module documentation
"""

from base import Base

class Rectangle(Base):
    """
    class documentation
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__int__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        getter documentation of rectangle
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        setter documentation of rectangle
        """
        self.__width = value

    @property
    def height(self):
        """
        getter documentation of rectangle
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        setter documentation of rectangle
        """
        self.__height = value

    @property
    def x(self):
        """
        getter documentation of rectangle
        """
        return self.__x
    
    @x.setter
    def x(self, value):
        """
        setter documentation of rectangle
        """
        self.__x = value

    @property
    def y(self):
        """
        getter documentation of rectangle
        """
        return self.__y
    
    @y.setter
    def y(self, value):
        """
        setter documentation of rectangle
        """
        self.__y = value