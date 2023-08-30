import fruit

class Orange(fruit.Fruit):

    def __init__(self, color, shape, acid_level=6):

        super().__init__(color, shape)
        self.color = color
        self.shape = shape
        self.acid_level = acid_level
    def print_all(self):
        print(f"orange class color {self.color} adn shape {self.shape} annd asid level = {self.acid_level}")
        





