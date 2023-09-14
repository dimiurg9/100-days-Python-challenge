"""
Black Jack game
"""
import random
from replit import clear
from art import logo

def another_game():
    """
    Ask if person would like to continue the game or quit
    :return: none #it will reiterate the game or quit
    """
    clear()
    if input("another game y/n \n") == "y":
        clear()
        play()
    else:
        exit()

def get_card():
    """
    Serve one card upon request
    :return: int card
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.sample(cards, 1)[0]
    print(f"Dealed {card}")
    return card

def compare(computer_final, player_final):
    """
    Compare two players final values
    :param computer_final:
    :param player_final:
    :return: int: status code
    """
    if computer_final > 21 and player_final > 21:
        return 1
    if player_final > 21 and computer_final < 22:
        return 4
    if computer_final <= 21 and computer_final > player_final:
        return 2
    if computer_final <= 21 and computer_final < player_final:
        return 3
    if computer_final < 21 and player_final < 21:
        if computer_final == player_final:
            return 6
    if computer_final > 21 and player_final < 22:
        return 7
    else:
        return 5


def is_ice(deal):
    """
    If player went bust, method check if there is an ice on players hands,
    if so, it will change ice value 11 into value 1
    :param deal: list of cards
    :return: list with changed values
    """
    for cards in deal:
        if cards == 11:
            deal.remove(11)
            deal.append(1)
    return deal

def player_turn(player_deal):
    """
    Promt player if another card should be served
    :param player_deal: list of card at first serve
    :return: final list of cards
    """
    current = player_deal
    while sum(player_deal) < 22:
        another_card = input(f"You have {sum(player_deal)} on hands. Another card? y/n \n")
        if another_card == "y":
            current.append(get_card())
            if sum(current) > 21:
                current = is_ice(current)
                player_turn(current)
            else:
                player_turn(current)
        if another_card == "n":
            return sum(current)
        else:
            return sum(current)
    return sum(current)

def computer_turn(computer_deal):
    """
    Makes dialer serve to itself until reach 17
    :param computer_deal: first serve list
    :return: final list of cards on dealers hands
    """
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
    """
    Main method to start the game and evaluate final results
    :return:
    """
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
    if compare(computer_final, player_final) == 6:
        print(f"Its a draw: Computer: {computer_final}. You: {player_final}")
    if compare(computer_final, player_final) == 7:
        print(f"You won: {computer_final}. You: {player_final}")
    if compare(computer_final, player_final) == 5:
        print(f"Computer: {computer_final}. You: {player_final}")


    another_game()

play()