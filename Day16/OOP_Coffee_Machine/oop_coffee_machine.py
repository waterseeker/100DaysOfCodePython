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
                total_coins_input = cashier.process_coins()
                drink_price = drink.cost
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
