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

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: The square description in the format [Square] (<id>) <x>/<y> - <size>.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

if __name__ == "__main__":
    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()