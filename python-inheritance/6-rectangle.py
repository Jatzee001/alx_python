#!/usr/bin/python3
"""6-rectangle.py"""
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


# Test cases
r = Rectangle(3, 5)
print(dir(r))
print(issubclass(Rectangle, BaseGeometry))

try:
    r = Rectangle(0, 4)
except ValueError as e:
    print(e)  # Output: width must be greater than 0

try:
    r = Rectangle(3, "3")
except TypeError as e:
    print(e)  # Output: height must be an integer

r = Rectangle(3, 5)
print(r._Rectangle__width)  # Output: 3
print(r._Rectangle__height)  # Output: 5

try:
    r = Rectangle()
except TypeError as e:
    print(e)  # Output: __init__() missing 2 required positional arguments: 'width' and 'height'