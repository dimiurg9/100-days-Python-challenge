import fruit
import orange


f = fruit.Fruit("orange", "square")
print(f.print_color_shape())

o = orange.Orange("red", "square", 3)
print(o.shape)
o.acid_level = 9
print(o.acid_level)

