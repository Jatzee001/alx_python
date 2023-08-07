class ClassBase:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            ClassBase.__nb_objects += 1
            self.id = ClassBase.__nb_objects

# Test the ClassBase functionality
if __name__ == "__main__":
    # Create an instance without passing an id (should assign id=1)
    obj1 = ClassBase()
    print(obj1.id)  # Output: 1

    # Create another instance without passing an id (should assign id=2)
    obj2 = ClassBase()
    print(obj2.id)  # Output: 2

    # Create an instance passing an id (should assign id=10)
    obj3 = ClassBase(10)
    print(obj3.id)  # Output: 10

    # Create another instance without passing an id (should assign id=3, which is 1 + 1)
    obj4 = ClassBase()
    print(obj4.id)  # Output: 3