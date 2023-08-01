"""
cound 1 - 100
if number devisible by 3 = fizz
if number devisible by 5 = buzz
if number devisible by 3 and 5 = fizzBuzz
"""

for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 == 0):
        print(f"{number} = fizzBuzz")
        # continue
    elif number % 3 == 0:
        print(f"{number} = fizz")
    elif number % 5 == 0:
        print(f"{number} = Buzz")
    else:
        print(number)
