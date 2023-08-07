# File: models/rectangle.py

class Base:
    def __init__(self, width, height, id=None):
        self.__width = width
        self.__height = height
        self.__id = id

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(width, height, id)
        self.__x = x
        self.__y = y

    # Getters and setters for private attributes
    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def get_id(self):
        return self._Base__id

    def set_id(self, id):
        self._Base__id = id

    # You can add specific methods or override methods from the Base class if needed
    # For example, if you want to customize the __str__ method for the Rectangle class:
    def __str__(self):
        return f"Rectangle (ID={self.get_id()}): width={self.get_width()}, height={self.get_height()}, area={self.area()}, perimeter={self.perimeter()}, x={self.get_x()}, y={self.get_y()}"