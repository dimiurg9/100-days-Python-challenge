#we can add function as a parametr

def add(a, b):
    return a + b

def substr(a,b):
    return a/b

def calculator(a, b, fun):
    return fun(a, b)

addition = calculator(2, 3, add)
print(addition)

substraction = int(calculator(6, 2, substr))
print(substraction)
