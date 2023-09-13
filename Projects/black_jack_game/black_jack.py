import random
from replit import clear
from art import logo

def another_game():
    clear()
    if input("another game y/n \n") == "y":
        clear()
        play()
    else:
        exit()

def get_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.sample(cards, 1)[0]
    print(f"dealed {card}")
    return card

def compare(computer_final, player_final):
    if computer_final > 21 and player_final > 21:
        return 1
    if player_final > 21 and computer_final < 22:
        return 4
    if computer_final <= 21 and computer_final > player_final:
        return 2
    if computer_final <= 21 and computer_final < player_final:
        return 3


def is_ice(deal):
    for cards in deal:
        if cards == 11:
            deal.remove(11)
            deal.append(1)
    return deal

def player_turn(player_deal):
    current = player_deal
    while sum(player_deal) < 22:
        another_card = input(f"you have {sum(player_deal)} on hands. Another card? y/n \n")
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
    print(logo)
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
    if sum(computer_deal) == 21 and len(computer_deal) == 2:
        print("Dealer has a Black Jack")
        another_game()

    computer_final = computer_turn(computer_deal)
    print(f"Dealer played with {computer_final}")

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