#!/usr/bin/python3
"""
Module models/rectangle: This module defines the Rectangle class.
"""

from models.base import Base

class Rectangle(Base):
    """
    Rectangle class inherits from Base and represents a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The horizontal position of the rectangle.
        __y (int): The vertical position of the rectangle.

    Public Methods:
        - __init__(self, width, height, x=0, y=0, id=None): Initializes a Rectangle instance.
        - area(self): Returns the area of the Rectangle instance.
        - display(self): Prints the Rectangle instance using the character '#'.
        - __str__(self): Returns the string representation of the Rectangle instance.
        - update(self, *args, **kwargs): Update the attributes of the Rectangle instance.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The horizontal position of the rectangle. Defaults to 0.
            y (int, optional): The vertical position of the rectangle. Defaults to 0.
            id (int, optional): The unique identifier of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # ... (Other methods)

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Rectangle instance.

        Args:
            *args: Variable number of positional arguments.
            **kwargs: Keyword arguments representing key/value pairs to update attributes.
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    # ... (Other methods)

if __name__ == "__main__":
    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=1)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)