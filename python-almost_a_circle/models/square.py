#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the square."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

# Sample usage
if __name__ == "__main__":
    square1 = Square(5)
    print(square1)
    
    square2 = Square(5, 7)
    print(square2)
    
    square3 = Square(5, 7, 2)
    print(square3)
    
    square4 = Square(5, 7, 2, 89)
    print(square4)
    
    print("Area:", square4.area())
    print("Display:")
    square4.display()