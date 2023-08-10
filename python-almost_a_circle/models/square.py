#!/usr/bin/python3

"""
Defines a square class
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square.
        """
        super().__init__(size, size, x=0, y=0, id=None)

    def __str__(self):
        """
        str doc
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Set/get the size of the Square."""
        return self.width
    
    @size.setter
    def size(self, value):
        """
        size setter method
        """

        self.width = value
        self.height = value