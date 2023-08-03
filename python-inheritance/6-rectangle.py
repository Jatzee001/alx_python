class BaseGeometry:
    """Base class for geometry.

    This class provides a base for other geometry classes to inherit from.

    """

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: Always raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the integer value.

        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A class representing a rectangle.

    This class inherits from BaseGeometry and adds functionality specific to rectangles.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
