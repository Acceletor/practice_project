from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
isdone = False
my_coffee_machine =CoffeeMaker()
my_money_machine = MoneyMachine()


options = my_menu.get_items()

while not isdone:
    choice = input(f"What would you like? {options}:")
    if choice == "report":
        my_coffee_machine.report()
        my_money_machine.report()
    elif choice == "off":
        isdone = True
    else:
        drink = my_menu.find_drink(choice)
        if choice == "latte" or choice =="espresso" or choice == "cappuccino":
            if my_coffee_machine.is_resource_sufficient(drink):
                if my_money_machine.make_payment(drink.cost):
                    my_coffee_machine.make_coffee(drink)
