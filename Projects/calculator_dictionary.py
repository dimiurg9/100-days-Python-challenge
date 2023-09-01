
def add(a,b):
    return a + b

def substract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b


operators = {
    "+": add, # type function
    "/": divide,
    "*": multiply,
    "-": substract,
}
first_number = int(input("What is first number? "))
second_number = int(input("What is second number? "))

for key in operators.keys():
    print(key)

picked_operator = input("pick operator")
print(type(operators["+"]))

picked_function = operators[picked_operator]
print(picked_function(first_number, second_number))



