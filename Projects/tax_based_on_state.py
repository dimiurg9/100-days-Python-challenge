"""
Create method which takes stated and income as an argument
and return incom after tax deduction
Fed tax = 10%
"""
taxes_by_state = {"CA": 3, "WA":5, "NY":12 }
fed_tax = 10

def gros_after_tax(state, gross_income):
    return gross_income - taxes_by_state[state]/100 * gross_income - fed_tax/100 * gross_income

def change_fed_tax_to9():
    global fed_tax
    fed_tax = 9

print(gros_after_tax("CA", 30000))
change_fed_tax_to9()
print(fed_tax)