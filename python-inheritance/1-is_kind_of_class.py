"""
second python inheritance task
"""
def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an instance of a class
    that inherited from, the specified class.
    """

    if type(obj) == a_class or issubclass(type(obj), a_class):
        return True
    else:
        return False
