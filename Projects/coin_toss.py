import Syntax.random_generate

coin_tossed = Syntax.random_generate.random_number(0,1)
if coin_tossed == 1:
    print("Tails")
else:print("Heads")

randomFloat = Syntax.random_generate.random_float(1.0, 5.0)
print(format(randomFloat, '.2f'))