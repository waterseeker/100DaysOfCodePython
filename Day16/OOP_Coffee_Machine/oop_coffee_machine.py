from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

play_game = True

while play_game:
    while True:
        user_input = input(
            " What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == 'off':
            play_game = False
            break
        elif user_input == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(user_input)
            enough_resources = coffee_maker.is_resource_sufficient(drink)
            if enough_resources is True:
                drink_price = drink.cost
                sufficient_funds = money_machine.make_payment(drink_price)
                coffee_maker.make_coffee(drink)
            continue
