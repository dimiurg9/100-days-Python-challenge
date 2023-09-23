from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True
options = menu.get_items()
while is_on:
    choise = input(f"What would you like? {options} ")
    if choise == "off":
        is_on = False
        exit()
    if choise == "report":
        money_machine.report()
        coffe_maker.report()
    drink = menu.find_drink(choise)
    if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        coffe_maker.make_coffee(drink)



