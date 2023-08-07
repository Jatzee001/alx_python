#!/usr/bin/python3

"""This is to write the first class base."""

class Base:
    """
    Base class for all future classes in this project.
    Manages the id attribute in all future classes and avoids duplicating the same code and bugs.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new instance of the Base class.
        
        Args:
            id (int): The ID of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects