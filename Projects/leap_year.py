"""
leap year calculator

A every year that is evenly divisible by 4
except every year that is evenly divisible by 100
unless the year is also evenly divisible by 400
"""

year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 != 0:
        print("leap")
    elif year % 100 == 0 and year % 400 == 0 :
        print("leap")
    else: print("not leap")
else: print("not leap")