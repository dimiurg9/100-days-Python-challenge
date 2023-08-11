#get all numbers from string and get avg

from statistics import mean

string_to_parce = "there are 9 nubers in here 5555"
number_from_sting = []
for i in string_to_parce:
    if i.isdigit():
        number_from_sting.append(int(i))
print("%.2f" % mean(number_from_sting))