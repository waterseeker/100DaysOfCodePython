from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
drink_menu = Menu()
cashier = MoneyMachine()

play_game = True

while play_game:
    while True:
        user_input = input(
            " What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == 'off':
            play_game = False
            break
        elif user_input == 'report':
            coffee_machine.report()
        elif drink is None:
            print("Sorry, that's not a valid choice. Try again.")
            continue
        else:
            drink = drink_menu.find_drink(user_input)
            enough_resources = coffee_machine.is_resource_sufficient(drink)
            if enough_resources is True:
                drink_price = drink.cost
                sufficient_funds = cashier.make_payment(drink_price)
                coffee_machine.make_coffee(drink)
            continue
