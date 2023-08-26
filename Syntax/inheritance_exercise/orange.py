import fruit

class Orange(fruit.Fruit):

    def __init__(self, color, shape, acid_level):

        super().__init__(color, shape)
        self.color = color
        self.shape = shape
        self.acid_level = acid_level
    def print_all(self):
        print(f"this orange class {self.color} and "
              f"{self.shape} and {self.acid_level}")




