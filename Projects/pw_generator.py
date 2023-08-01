#todo: (done) refactore to random.choise instead of random.randomint
#todo: (done) for hard way pw to use random.shuffle()
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# letters_string = ""
# symbols_str = ""
# numbers_string = ""
pw_random = []
# pw_list = []

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for let in range(0, nr_letters):
    pw_random.append(str((random.choice(letters))))
    #my version:
    # pw_random.insert(random.randint(0,len(pw_random)), str(letters[random.randint(0,len(letters)-1)]) )
    # letters_string += str(letters[random.randint(0,len(letters)-1)])

for let in range(0, nr_symbols):
    pw_random.append(str(random.choice(symbols)))
    # pw_random.insert(random.randint(0,len(pw_random)), str(symbols[random.randint(0,len(symbols)-1)]) )
    # symbols_str += str(symbols[random.randint(0,len(symbols)-1)])

for let in range(0, nr_numbers):
    pw_random.append(str(random.choice(numbers)))
    # pw_random.insert(random.randint(0,len(pw_random)), str(numbers[random.randint(0,len(numbers)-1)]) )
    # numbers_string += str(numbers[random.randint(0,len(numbers)-1)])

# pw = letters_string + symbols_str + numbers_string
pw_string = ""
for pw in pw_random:
    pw_string += pw
print("eazy pw: " + pw_string)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
pw_shuffled = random.shuffle(pw_random)
hard_pw = ""
for i in pw_random:
    hard_pw += i

print("hard pw: " + hard_pw)