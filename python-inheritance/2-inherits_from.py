# my_module.py

def inherits_from(obj, a_class):
    """Check if the object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of a subclass of the specified class; otherwise False.

    Example:
        class MyBaseClass:
            pass

        class MySubClass(MyBaseClass):
            pass

        obj = MySubClass()

        print(inherits_from(obj, MyBaseClass))  # Output: True (MySubClass is a subclass of MyBaseClass)
        print(inherits_from(obj, MySubClass))   # Output: False (obj is not a subclass of MySubClass)
        print(inherits_from(obj, object))      # Output: True (MySubClass is a subclass of object)
    """
    return isinstance(obj, type) and issubclass(type(obj), a_class) and type(obj) is not a_class