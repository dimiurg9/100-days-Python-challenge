import fruit
import orange


f = fruit.Fruit("orange", "square")
fruit_print = f.print_color_shape()
print(fruit_print)

o = orange.Orange("red", "sircle", 3)
print(o.acid_level)

o.acid_level = 9
print(o.acid_level)
o.print_all()

