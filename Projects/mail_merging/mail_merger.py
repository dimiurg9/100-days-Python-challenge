"""
Create a ready to send letters in separate files using starting_letter.txt
and insert the names from names.txt
Create separate txt file ready to send
"""
path_to_names = "names/names.txt"
path_to_ready_to_send_directory = "ready_to_send/"
path_to_starting_letter = "names/starting_letter.txt"
PLACEHOLDER = "[name]"

def starting_letter_content():
    with open(path_to_starting_letter, 'r') as starting_letter:
        starting_letter_unmodified = starting_letter.read()
        return starting_letter_unmodified

def mail_merger(path_to_names):
    with open(path_to_names, 'r') as names:
        for name in names:
            content = mail_content(name)
            file_name = "invite_" + name
            create_ready_to_send_file(file_name, content)
    print("**************************")
    print("Letters are ready to send")

def mail_content(name):
    mail_content_unmodified = starting_letter_content()
    mail_content_modified = mail_content_unmodified.replace(PLACEHOLDER, name.strip())
    return mail_content_modified

def create_ready_to_send_file(file_name, content):
    file_path = path_to_ready_to_send_directory + file_name
    with open(file_path, 'w') as mail_file:
        mail_file.write(content)


mail_merger(path_to_names)