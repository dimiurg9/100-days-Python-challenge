""" pizza order """
SMALL_PIZZA = 15
MEDIUM_PIZZA = 20
LARGER_PIZZA = 25
bill = 0

size = int(input("Which size? 1 for small, 2 for medium, 3 for large: "))
peperoni = input("Do you like peperoni? y/n: ")

if size == 1:
    bill = SMALL_PIZZA
    if peperoni == "y":
        bill += 2
elif size == 2:
    bill = MEDIUM_PIZZA
    if peperoni == "y":
        bill += 3
elif size == 3:
    bill = LARGER_PIZZA
    if peperoni == "y":
        bill += 3

print(f"Your bill is {bill}")





