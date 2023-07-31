"""
in dictionary of student get all student of grade 1 heights and make it average
correct answer: 171,6
"""
Adam = {"grade":1, "heigh": 180}
Paylik = {"grade":2, "heigh": 150}
Vanyatko = {"grade":1, "heigh": 160}
Ueban = {"grade":1, "heigh": 175}

students_list = [Adam, Paylik, Vanyatko, Ueban]
studens_heits = []

for names in students_list:
    if names["grade"] == 1:
        studens_heits.append(names["heigh"])

print(round(sum(studens_heits) / len(studens_heits), 2))




