#!/usr/bin/python3
"""
Module models/square: This module defines the Square class.
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Square class inherits from Rectangle and represents a square.

    Public Methods:
        - __init__(self, size, x=0, y=0, id=None): Initializes a Square instance.
        - __str__(self): Returns the string representation of the Square instance.
        - size (property): Getter for the size attribute.
        - size (setter): Setter for the size attribute.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The horizontal position of the square. Defaults to 0.
            y (int, optional): The vertical position of the square. Defaults to 0.
            id (int, optional): The unique identifier of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): The new size value to set.
        """
        self.width = value
        self.height = value

if __name__ == "__main__":
    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))