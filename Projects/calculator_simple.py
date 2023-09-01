""""
To calculate two numbers from the input.
The operator is from the input as well
"""

def calculation(first_number, second_number, picked_operator):
    """
    The method calculates the passed parameters and return result double
    :param first_number: int
    :param second_number:
    :param picked_operator: *+-/
    :return: float
    """
    if picked_operator == "+":
        return first_number + second_number
    elif picked_operator == "-":
        return first_number - second_number
    elif picked_operator == "*":
        return first_number * second_number
    elif picked_operator == "/":
        if second_number == 0:
            print("Can not devide by 0")
            exit()
        else:
            return first_number / second_number

def get_inputs():
    first_number = int(input("What is the first number? "))
    second_number = int(input("What is the second number? "))
    picked_operator = input("What operator? ")
    result = calculation(first_number, second_number, picked_operator)
    print(result)

get_inputs()
