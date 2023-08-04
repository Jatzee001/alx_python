#!/usr/bin/python3
"""6-rectangle.py"""

class BaseGeometry:
    def area(self):
        raise NotImplementedError("Subclasses must implement the 'area' method.")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement the 'perimeter' method.")

    @staticmethod
    def integer_validator(name, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer.")


# rectangle.py
from base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)