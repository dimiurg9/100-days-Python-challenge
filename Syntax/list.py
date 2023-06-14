
fruits = ["apple", "orange"]
veggies = ["Spinach", "kale"]

fruits.append("Peaches")
fruits[0] = "Apple"
print(fruits[1])
print("Last item in list: " + fruits[-1])
print("with -2: " + fruits[-2])
print(fruits)
print(type(fruits))

# nested list

fruits_and_veggies = [fruits, veggies]
print(fruits_and_veggies[1][1])
# should print kale

