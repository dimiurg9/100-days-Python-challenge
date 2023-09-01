
my_dictionary = {
    "a": ["aa", "bb", "cc"],
    "b":{
        "x":"xx",
        "y":"yy",
        "z":"zz"
    }
}

print(my_dictionary["a"][1])
print(my_dictionary["b"]["y"])
my_dictionary["b"]["y"] = "bbbbbbb"
print(my_dictionary["b"]["y"])