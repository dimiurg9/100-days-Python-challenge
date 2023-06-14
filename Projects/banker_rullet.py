"""
input is the names with the commas
output is one person picked who pay the bill
"""
import random

names = input("Enter names with the commas: ")
participants = names.split(",")
randomNumber = random.randint(0, len(participants)-1)
print(f"{participants[randomNumber]} is paying the bill")