"""
Body mass index (BMI) is a value derived from the mass (weight) and height of a person.
The BMI is defined as the body mass divided by the square of the body height,
and is expressed in units of kg/m2, resulting from mass in kilograms and height in metres.
height feets to meters: 0.304
weight lb to kg: m/2.205
"""

weight = int(input("What is you weight in pounds? "))
height = float(input("What is your height in inches?  "))
printBMI = "your BMI is: {BMI:.2f}"
print(printBMI.format(BMI = (weight/2.205)/(height * 0.302)**2))

print("using round " + str(round((weight/2.205)/(height * 0.302)**2, 2 )))
