nameLength = len(input("what is you name? "))
print(type(nameLength))

# no error
print(f"your name have {nameLength} characters")

#TypeError: can only concatenate str (not "int") to str
# print("name " + nameLength + " characters")

# print("name " + str(nameLength)+ " characters")

a, b, c = 1, 2, "c"
#if we don't care about some of values, we can use decoratior
# we can use a, _, _ = return_three_values()

print(f"a = {a}, b = {b}, c = {c}")
