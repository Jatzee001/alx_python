"""
improve geometry inheritance task
"""
class BaseGeometryMeta(type):
    def __dir__(self):
        variables = super().__dir__()
        new_variables = [
            var for var in variables if var != "__int_subclass__"]
        return new_variables
        
class BaseGeometry(metaclass=BaseGeometryMeta):
    """
    non empty class
    """

    def __dir__(self):
        variables = super().__dir__()
        new_variables = [
            var for var in variables if var != "__int_subclass__"]
        return new_variables

    def area(self):
        raise NotImplementedError("area() is not implemented")
    
    # Test cases

# Test case 1: bg = BaseGeometry()
bg = BaseGeometry()
print(dir(bg))

# Test case 2: bg = BaseGeometry()
# This will raise a NotImplementedError since area() is not implemented in BaseGeometry.
bg = BaseGeometry()
try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))