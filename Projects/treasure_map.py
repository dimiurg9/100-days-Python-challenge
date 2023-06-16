"""
Prompted user for location
and check if the treasure is there
"""
import random

def inputMethod()-> bool:
    first_row = [" ", " ", " "]
    second_row = [" ", " ", " "]
    third_row = [" ", " ", " "]
    all_rows = [first_row, second_row, third_row]

    print ("     1    2    3")
    print(f" 1 {first_row}\n 2 {second_row}\n 3 {third_row}")

    random_row = random.randint(1, 3)
    random_column = random.randint(1, 3)

    user_column = int(input("Where is the treasure? \nEnter column 1-3: "))
    user_row = int(input("Enter row 1-3: "))

    if user_row == random_row and user_column == random_column:
        all_rows[random_row -1][random_column -1] = "V"
        print(f" 1 {first_row}\n 2 {second_row}\n 3 {third_row}")
        print("You found the treasure!!!")
    else:
        all_rows[random_row -1][random_column -1] = "V"
        all_rows[user_row -1 ][user_column -1] = "X"
        print(f" 1 {first_row}\n 2 {second_row}\n 3 {third_row}")
        print("No treasure here")

    try_again = input("Whant to try again? y/n: ")
    if "y" in try_again:
        return True
    else: return False



print(" Welcome to treasure hunting!\n")
if inputMethod():
    inputMethod()
else: exit()














