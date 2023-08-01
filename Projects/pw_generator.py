#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letters_random = []
letters_string = ""
symbols_random = []
symbols_str = ""
number_random = []
numbers_string = ""
pw_random = []

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for let in range(0, nr_letters):
    pw_random.insert(random.randint(0,len(pw_random)), str(letters[random.randint(0,len(letters)-1)]) )
    letters_string = letters_string + str(letters[random.randint(0,len(letters)-1)])

for let in range(0, nr_symbols):
    pw_random.insert(random.randint(0,len(pw_random)), str(symbols[random.randint(0,len(symbols)-1)]) )
    symbols_str = symbols_str + str(symbols[random.randint(0,len(symbols)-1)])

for let in range(0, nr_numbers):
    pw_random.insert(random.randint(0,len(pw_random)), str(numbers[random.randint(0,len(numbers)-1)]) )
    numbers_string = numbers_string + str(numbers[random.randint(0,len(numbers)-1)])

pw = letters_string + symbols_str + numbers_string
print("eazy pw: " + pw)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_pw = ""
for i in pw_random:
    hard_pw = hard_pw + i

print("hard pw: " + hard_pw)