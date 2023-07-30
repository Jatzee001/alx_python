def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class.

    This function takes an object and a class as input arguments and checks
    if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of the specified class; otherwise False.

    Example:
        class MyClass:
            pass

        class AnotherClass:
            pass

        obj1 = MyClass()
        obj2 = AnotherClass()

        print(is_same_class(obj1, MyClass))  # Output: True
        print(is_same_class(obj2, AnotherClass))  # Output: True
        print(is_same_class(obj1, AnotherClass))  # Output: False
        print(is_same_class(obj2, MyClass))  # Output: False
    """
    return type(obj) is a_class