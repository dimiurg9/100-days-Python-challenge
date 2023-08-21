import random
import linecache

def modify_original_to_hidden(word_list_original):
    count_letter = 0
    for i in range(len(word_list_original)):
        word_list_original[count_letter] = "-"
        count_letter += 1
    return word_list_original

def get_word() -> str:
    with open('wordlist.txt', 'r') as fp:
        number_of_words = len(fp.readlines())
        word = linecache.getline('wordlist.txt', random.randint(1, number_of_words))
        return word

def is_letter_in_word(word,word_list_modified, letter):
    count_letter = 0
    list_a = word_list_modified
    for i in word:
        if i == letter:
            list_a[count_letter] = letter
            count_letter += 1
        else:
            count_letter += 1
            continue

    return list_a

def continue_game():
    continue_game = input("Want to continue? y/n:")
    if continue_game == "n":
        print("See you next time")
        exit()
    if continue_game == "y":
        return True
    else:
        print("incorrect input")
        exit()
def get_state(number):
    # pictures downloaded from https://codereview.stackexchange.com/questions/43318/python-hangman-program
    state = [
        [
            '\t  _______ ',
            '\t  |     | ',
            '\t        | ',
            '\t        | ',
            '\t        | ',
            '\t        | ',
            '\t________|_',
        ],
        [
            '\t  _______ ',
            '\t  |     | ',
            '\t  O     | ',
            '\t        | ',
            '\t        | ',
            '\t        | ',
            '\t________|_',
        ],
        [
            '\t  _______ ',
            '\t  |     | ',
            '\t  O     | ',
            '\t  |     | ',
            '\t  |     | ',
            '\t        | ',
            '\t________|_',
        ],
        [
            '\t  _______ ',
            '\t  |     | ',
            '\t  O     | ',
            '\t \|     | ',
            '\t  |     | ',
            '\t        | ',
            '\t________|_',
        ],
        [
            '\t  _______ ',
            '\t  |     | ',
            '\t  O     | ',
            '\t \|/    | ',
            '\t  |     | ',
            '\t        | ',
            '\t________|_',
        ],
        [
            '\t  _______ ',
            '\t  |     | ',
            '\t  O     | ',
            '\t \|/    | ',
            '\t  |     | ',
            '\t /      | ',
            '\t________|_',
        ],
        [
            '\t  _______ ',
            '\t  |     | ',
            '\t  O     | ',
            '\t \|/    | ',
            '\t  |     | ',
            '\t / \\    | ',
            '\t________|_',
        ]
    ]
    return state[number]