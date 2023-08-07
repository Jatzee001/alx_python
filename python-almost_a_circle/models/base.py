class ClassBase:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            ClassBase.__nb_objects += 1
            self.id = ClassBase.__nb_objects