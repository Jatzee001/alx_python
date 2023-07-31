class BaseGeometry:
    """
    Base class for geometry.

    This class provides a base for other geometry classes to inherit from.

    Methods:
        area(self): Raises an Exception with the message "area() is not implemented".
        integer_validator(self, name, value): Validates the integer value.

    Attributes:
        name: The name of the value being validated.
        value: The integer value to be validated.
    """

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: Always raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the integer value.

        Args:
            name (str): The name of the value being validated.
            value: The integer value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

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

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Generate the string representation of the rectangle.

        Returns:
            str: The formatted string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


# Test cases
print(dir(Rectangle))

r = Rectangle(1, 4)
print(r.area())  # Output: 4

r = Rectangle(1411, 781)
print(r.area())  # Output: 1103191

r = Rectangle(5, 5)
print(r.area())  # Output: 25

r = Rectangle(1411, 781)
print(r)  # Output: [Rectangle] 1411/781

r = Rectangle(1, 4)
print(r)  # Output: [Rectangle] 1/4

r = Rectangle(5, 5)
print(r)  # Output: [Rectangle] 5/5

r = Rectangle()
# Output: TypeError: __init__() missing 2 required positional arguments: 'width' and 'height'