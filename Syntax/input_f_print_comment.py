#len input f comments
word = input("Enter word here: \n")
word_length = len(word)
print(f"In word {word} are {word_length} characters \n" * 3)


# format money so only 2 digits after dot
bill = 20.55444444
print_total = "Each person should pay: ${price:.2f}"
print(print_total.format(price = bill))

"""
Enter word here: asdfvas
In word asdfvas are 7 characters 
In word asdfvas are 7 characters 
In word asdfvas are 7 characters 

Each person should pay: $20.55
"""