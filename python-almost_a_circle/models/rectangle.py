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
        - update(self, *args): Update the attributes of the Rectangle instance.
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

    def update(self, *args):
        """
        Update the attributes of the Rectangle instance.

        Args:
            *args: Variable number of arguments to update the attributes in the order:
                   id, width, height, x, y
        """
        num_args = len(args)
        if num_args > 0:
            self.id = args[0]
        if num_args > 1:
            self.width = args[1]
        if num_args > 2:
            self.height = args[2]
        if num_args > 3:
            self.x = args[3]
        if num_args > 4:
            self.y = args[4]

    # ... (Other methods)

if __name__ == "__main__":
    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(89)
    print(r1)

    r1.update(89, 2)
    print(r1)

    r1.update(89, 2, 3)
    print(r1)

    r1.update(89, 2, 3, 4)
    print(r1)

    r1.update(89, 2, 3, 4, 5)
    print(r1)