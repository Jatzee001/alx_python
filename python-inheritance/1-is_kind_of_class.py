"""
second python inheritance task
"""
def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an instance of a class
    that inherited from, the specified class.
    """

    if obj.__class__.__name__ == a_class.__name__:
        return True
    else:
        return type(obj) == a_class

    

