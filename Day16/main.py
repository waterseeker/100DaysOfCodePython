from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def get_drink_choice():
    """Gets user input to select a drink. Returns the drink item from the
    MENU. Returns False if user inputs 'off'"""
    drink_choice = input("What would you like? (espresso/latte/cappuccino):\n")
    cleaned_drink_choice = drink_choice.strip().lower()
    if cleaned_drink_choice == "off":
        return cleaned_drink_choice
    elif cleaned_drink_choice == "report":
        # print out report of resource balances
        return cleaned_drink_choice
    elif cleaned_drink_choice not in menu.get_items():
        print("Please select espresso, latte, or cappuccino.")
        return get_drink_choice()
    else:
        return cleaned_drink_choice


is_operating = True

while is_operating:
    drink_choice = get_drink_choice()
    if drink_choice == "off":
        is_operating = False
        break
    elif drink_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(drink_choice)
        # check resources
        enough_resources = coffee_maker.is_resource_sufficient(drink)
        if enough_resources:
            # take money
            enough_money = money_machine.make_payment(drink.cost)
            if enough_money:
                # use resources
                # serve drink
                coffee_maker.make_coffee(drink)
