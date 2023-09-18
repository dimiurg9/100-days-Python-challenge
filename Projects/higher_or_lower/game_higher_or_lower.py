"""
Game to compare followers count in social media for two persons
"""
import random
import game_data
import art


def game(score):
    """
    Get the random pieces of data and compare the data with user input
    :param score:
    :return: none
    """
    objects = random.sample(game_data.data, 2)
    a_object = objects[0]
    b_object = objects[1]
    score = score
    print(f"Compare A: {a_object.get('name')}, {a_object.get('description')} from {a_object.get('country')}")
    # print vs art
    print(art.vs)
    # print second set of data as B
    print(f"Compare B: {b_object.get('name')}, {b_object.get('description')} from {b_object.get('country')}")
    # ask user who has more followers, to type A or B
    # print(f"A: {a_object.get('follower_count')}, B: {b_object.get('follower_count')}")
    print(f"Current score: {score}")
    user_guess = input("Who has more followers? Type A or B: ")

    if a_object.get('follower_count') > b_object.get('follower_count'):
        correct_answer = "A"
    else:
        correct_answer = "B"

    if user_guess == correct_answer:
        score += 1
        print(f"You are right. Current score = {score}")
        game(score)
    else:
        print(f"Sorry, that's wrong. Final score {score}")
        exit()


print(art.logo)
game(0)
