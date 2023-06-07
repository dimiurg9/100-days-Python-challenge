print("Velcome to tip calculator")
"""
1. ask about amount
2. ask about persons to split the bill
3. how many % tip 10, 15, 20 etc
4. calculate how much everyone have to pay
"""

total_bill = float(input("What was the total bill? $"))
number_of_persons = int(input("How many peoples to split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_amount = total_bill / 100 * tip_percentage
split_bill = (total_bill + tip_amount)/number_of_persons
print_total = "Each person should pay: ${price:.2f}"
print(print_total.format(price = split_bill))