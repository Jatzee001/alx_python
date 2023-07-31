class BaseGeometry:
    """Base class for geometry.

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

        Example:
            >>> bg = BaseGeometry()
            >>> bg.integer_validator("width", 10)  # Valid
            >>> bg.integer_validator("height", "invalid")  # Raises TypeError
            >>> bg.integer_validator("side_length", 0)  # Raises ValueError
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")