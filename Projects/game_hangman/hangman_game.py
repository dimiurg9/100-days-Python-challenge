import utils
from replit import clear #to clear console and avoid scrolling
def game():
    word = utils.get_word()
    word_list_original = list(word)[:-1]
    word_list_modified = utils.modify_original_to_hidden(word_list_original)
    print(word_list_modified)

    dead_count = 0
    while dead_count < 7:
        clear()
        letter = input("Guess a letter: ")
        if letter in word:
            print(f"there is letter {letter} in word")
            word_list_modified = utils.is_letter_in_word(word, word_list_modified, letter)
            print(word_list_modified)
            if "-" in word_list_modified:
                continue
            else:
                print("you won!")
                if utils.continue_game():
                    game()

        else:
            print(f"There is no letter \" {letter} \" in this word")
            state = utils.get_state(dead_count)
            for i in state:
                print(i + '\n')
            dead_count += 1
            print(word_list_modified)
            if dead_count == 7:
                print("GAME OVER")
                print("The word was:" + word)

                if utils.continue_game():
                    game()
game()







