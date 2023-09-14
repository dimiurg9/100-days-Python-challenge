"""
gues the number with 2 difficulty levels
"""

import random

DIFFICULT_EFFORTS = 5
EASY_EFFORTS = 10


def get_number():
    """
    get random number
    :return: int
    """
    number = random.randint(1, 100)
    return number


def guess(number):
    """
    Asking user to guess the number
    :param number:
    :return: boolean
    """
    guess_number = int(input("what is a number? "))
    if number == guess_number:
        return True
    if guess_number > number:
        print("lower")
        return False
    if guess_number < number:
        print("higher")
        return False


def play_again():
    """
    Ask if user wants to play again or end game
    :return:
    """
    if input("Play again? y/n ") == "y":
        play()
    else:
        exit()


def play():
    """
    Starting game. Asking user what is the difficulty level
    Allowed number of guesses based on difficulty level
    :return:
    """
    print("Welcome to the Number Guessing game")
    print("I am thinking of a number from 1 to 100")
    # print(f"Debug: number {thinking_number}")
    diff = int(input("Select difficulty: 1 for EASY, 2 for HARD \n"))
    guesses_total = 0
    if diff == 1:
        guesses_total = EASY_EFFORTS
    if diff == 2:
        guesses_total = DIFFICULT_EFFORTS

    print(f"You have {guesses_total} guesses")

    guesses = 0
    thinking_number = get_number()
    for i in range(0, guesses_total):
        effort = guess(thinking_number)
        if not effort:
            guesses += 1
            print(f"Guesses left: {guesses_total - guesses}")
        if effort:
            print("you won")
            play_again()
    print("You loose")
    play_again()


play()
