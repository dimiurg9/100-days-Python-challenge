import utils

def game():
    word = utils.get_word()
    # print(word)
    word_list_original = list(word)[:-1]
    # print(word_list_original)
    word_list_modified = utils.modify_original_to_hidden(word_list_original)
    print(word_list_modified)

    dead_count = 0
    while dead_count < 7:
        letter = input("Guess a letter: ")
        if letter in word:
            print(f"there is letter {letter} in word")
            word_list_modified_a = utils.is_letter_in_word(word, word_list_modified, letter)
            word_list_modified_a = word_list_modified
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
            if dead_count == 7:
                print("GAME OVER")
                print("The word was:" + word)
                if utils.continue_game():
                    game()


game()







