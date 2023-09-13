import random
from replit import clear

def another_game():
    clear()
    print("")
    print("")
    print("another_game ######")
    if input("another game y/n") == "y":
        clear()
        play()
    else:
        exit()

def get_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.sample(cards, 1)[0]
    print(f"dealed {card}")
    return card

# def play(total):
#     print("play ######")
#     player_total = total
#     while player_total < 22:
#         play_more = str(input("another card? y/n "))
#         if play_more == "y":
#             another_card = get_card()
#             player_total = total + another_card
#             print(f"your card is {another_card} and yur total is: {player_total}")
#             if player_total > 21:
#                 return player_total
#         else:
#             return player_total
#     return player_total

# def computer_play(computer_deal):
#     print("Computer_play ######")
#     computer_total = computer_deal
#     while computer_total < 17:
#         random_card = get_card()
#         computer_total = computer_deal + random_card
#         print(f"random card {random_card}")
#     print(f"computer total is {computer_total}")
#     return computer_total

def compare(computer_final, player_final):
    print("compare executing")
    # if computer_final == 21 and len(computer_final) == 2:
    #     return 0
    if computer_final > 21 and player_final > 21:
        return 1
    if computer_final <= 21 and computer_final > player_final:
        return 2
    if computer_final <=21 and computer_final < player_final:
        return 3
    if player_final > 21 and computer_final < 22:
        return 4

def is_ice(deal):
    for cards in deal:
        if cards == 11:
            deal.remove(11)
            deal.append(1)
    return deal

def player_turn(player_deal):
    current = player_deal
    while sum(player_deal) < 22:
        another_card = input(f"you have {sum(player_deal)} on hands. Another card? y/n")
        if another_card == "y":
            current.append(get_card())
            if sum(current) > 21:
                current = is_ice(current)
            else:
                player_turn(current)
        if another_card == "n":
            return sum(current)
        else:
            return sum(current)
    return sum(current)

def computer_turn(computer_deal):
    print("computer turn executed")
    current = computer_deal
    while sum(current) < 17:
        current.append(get_card())
    if sum(current)> 21:
        current = is_ice(current)
        if sum(current) < 17:
            computer_turn(current)
    else:
        return sum(current)
    return sum(current)

def play():
    computer_deal = []
    player_deal = []
    for i in range(2):
        computer_deal.append(get_card())
        player_deal.append(get_card())

    print(f"Dealer cards:  * ,  {computer_deal[1]}")
    print(f"Player cards: {player_deal[0]}, {player_deal[1]} total: {sum(player_deal)}")
    print("******************************************")

    player_final = player_turn(player_deal)
    print(f"player final {player_final}")
    computer_final = computer_turn(computer_deal)

    if compare(computer_final, player_final) == 0:
        print("Dealer has a Black Jack")
    if compare(computer_final, player_final) == 1:
        print(f"Draw. Both players bust: computer {computer_final} and player {player_final}")
    if compare(computer_final, player_final) == 2:
        print(f"Dealer won! Dealer: {computer_final} and player {player_final}")
    if compare(computer_final, player_final) == 3:
        print(f"You won! Computer: {computer_final}. You: {player_final}")
    if compare(computer_final, player_final) == 4:
        print(f"You bust! Computer: {computer_final}. You: {player_final}")

    another_game()

play()