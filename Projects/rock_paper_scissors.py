"""
0 for rock, 1 for paper, 2 for scissors
"""
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



comp_random = random.randint(0, 2)
choise = int(input("Select 0 for rock, 1 for paper, 2 for scissors: "))
moves = [rock, paper, scissors]

if choise == comp_random:
    print("you are equal")
    print("Your choise: " +  moves[choise])
    print("Computer choise: " + moves[comp_random])
    exit()

if choise == 0 and comp_random == 2:
    print("You Won!")
    print("Your choise: " +  moves[choise])
    print("Computer choise: " + moves[comp_random])
    exit()
if choise == 1 and comp_random == 0:
    print("You Won!")
    print("Your choise: " +  moves[choise])
    print("Computer choise: " + moves[comp_random])
    exit()
if choise == 2 and comp_random == 1:
    print("You Won!")
    print("Your choise: " +  moves[choise])
    print("Computer choise: " + moves[comp_random])
    exit()
else:
    print("You Loose  :(")
    print("___________")
    print("Your choise: " +  moves[choise])
    print("Computer choise: " + moves[comp_random])




