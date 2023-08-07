# File: models/rectangle.py

class Base:
    def __init__(self, width, height, id=None):
        """
        Base class constructor.

        Args:
            width (int): The width of the shape.
            height (int): The height of the shape.
            id (int, optional): The identifier for the shape. Defaults to None.
        """
        self.__width = width
        self.__height = height
        self.__id = id

    def area(self):
        """
        Calculate the area of the shape.

        Returns:
            int: The calculated area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the shape.

        Returns:
            int: The calculated perimeter.
        """
        return 2 * (self.__width + self.__height)


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Rectangle class constructor.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle. Defaults to 0.
            id (int, optional): The identifier for the rectangle. Defaults to None.
        """
        super().__init__(width, height, id)
        self.__x = x
        self.__y = y

    # Getters and setters for private attributes (width, height, x, y, and id) are not documented
    # as their purposes are self-explanatory from their names.

    def __str__(self):
        """
        String representation of the Rectangle.

        Returns:
            str: The formatted string representation.
        """
        return f"Rectangle (ID={self.get_id()}): width={self.get_width()}, height={self.get_height()}, area={self.area()}, perimeter={self.perimeter()}, x={self.get_x()}, y={self.get_y()}"