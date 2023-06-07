nameLength = len(input("what is you name? "))
print(type(nameLength))

# no error
# print(f"your name have {nameLength} characters")

#TypeError: can only concatenate str (not "int") to str
# print("name " + nameLength + " characters")

print("name " + str(nameLength)+ " characters")