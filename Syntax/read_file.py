"""
practicing to print particular string out of file

"""
STRING_TO_SEARCH = "True"
PATH = "/Users/slizhd/workspaces/100-days-Python-challenge/Projects/quiz_game/data.py"
def read_data_from_quiz_game(path):
    with open(path, 'r') as quiz:
        for line in quiz:
            if STRING_TO_SEARCH in line:
                print(line)


read_data_from_quiz_game(PATH)
