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
        drink = drink_menu.find_drink(user_input)
        if user_input == 'off':
            play_game = False
            break
        elif user_input == 'report':
            coffee_machine.report()
        elif drink is None:
            print("Sorry, that's not a valid choice. Try again.")
            continue
        else:
            enough_resources = coffee_machine.is_resource_sufficient(drink)
            if enough_resources is True:
                # TODO use money_machine here
                while True:
                    try:
                        number_of_quarters = int(input("how many quarters?: "))
                        break
                    except ValueError:
                        print("Sorry, you have to input a number.")
                        continue
                while True:
                    try:
                        number_of_dimes = int(input("how many dimes?: "))
                        break
                    except ValueError:
                        print("Sorry, you have to input a number.")
                        continue
                while True:
                    try:
                        number_of_nickels = int(input("how many nickles?: "))
                        break
                    except ValueError:
                        print("Sorry, you have to input a number.")
                        continue
                while True:
                    try:
                        number_of_pennies = int(input("how many pennies?: "))
                        break
                    except ValueError:
                        print("Sorry, you have to input a number.")
                        continue
                drink_price = MENU[user_input]["cost"]
                total_coins_input = (number_of_quarters * 0.25 +
                                     number_of_dimes * 0.10 +
                                     number_of_nickels * 0.05 +
                                     number_of_pennies * 0.01)
                if total_coins_input < drink_price:
                    print("Sorry that's not enough money. Money refunded.")
                    break
                elif total_coins_input >= drink_price:
                    resources["water"] -= (MENU[user_input]
                                               ["ingredients"]
                                               ["water"])
                    resources["coffee"] -= (MENU[user_input]
                                                ["ingredients"]
                                                ["coffee"])
                    if "milk" in MENU[user_input]["ingredients"]:
                        resources["milk"] -= (MENU[user_input]
                                                  ["ingredients"]
                                                  ["milk"])
                    if total_coins_input > drink_price:
                        change = round(total_coins_input - drink_price, 2)
                        print(f"Here is {change} dollars in change.")
                        resources["money"] += drink_price
                    drink_name = user_input
                    print(f"Here is your {drink_name} {coffee_emoji}. Enjoy!")
            continue
