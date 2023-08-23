a = 10
b = "aaa"

def changing_global_variable():
    global a, b
    a = 2
    b = "bbb"

print("a before calling method: " + str(a))
print("b before calling method: " + b)
changing_global_variable()
print("a after calling method: " + str(a))
print("b after calling method: " + b)