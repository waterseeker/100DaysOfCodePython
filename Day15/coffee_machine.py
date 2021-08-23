MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

coffee_emoji = '☕'
play_game = True

while play_game:
    while True:
        user_input = input(
            " What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == 'off':
            play_game = False
            break
        elif user_input == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']}")
        elif user_input not in MENU.keys():
            print("Sorry, that's not a valid choice. Try again.")
            continue
        else:
            enough_resources = {"water": True,
                                "coffee": True,
                                "milk": True}
            if resources["water"] - (MENU[user_input]
                                         ["ingredients"]
                                         ["water"]) < 0:
                enough_resources["water"] = False
                print("Sorry there is not enough water.")
                break
            if resources["coffee"] - (MENU[user_input]
                                          ["ingredients"]
                                          ["coffee"]) < 0:
                enough_resources["coffee"] = False
                print("Sorry there is not enough coffee.")
                break
            if "milk" in MENU[user_input]["ingredients"]:
                if resources["milk"] - (MENU[user_input]
                                            ["ingredients"]
                                            ["milk"]) < 0:
                    enough_resources["milk"] = False
                    print("Sorry there is not enough milk.")
                    break
            if False not in enough_resources.values():
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
            continue
#   a. Check the user's input to decide what to do next.
#   b. The prompt should show every time action has completed, e.g. once the
#       drink is dispensed. The prompt should show again to serve the next
#       customer.
# // TODO 5 - Process coins.
#   a. If there are sufficient resources to make the drink selected,
#       then the program should prompt the user to insert coins.
#   b. Remember tat quarters = $0.25, dimes = $0.10, nickels = $0.05,
#       and pennies = $0.01
#   c. Calculate the monetary value of the coins inserted. E.g. 1 quarter,
#       2 dimes, 1 nickel, 2 pennies = 0.25 + 2 * .10 + .05 + .01 * 2 = $0.52
#   d. Prompt the user: (each of these on a new line)
#       "how many quarters?: "
#       "how many dimes?: "
#       "how many nickles?: "
#       "how many pennies?: "
# // TODO 6 - Check transaction successful?
#   a. Check that the user has inserted enough money to purchase the drink
#       they selected. E.g. Latte cost $2.50, but they only inserted $0.52
#       then the program should say "Sorry that's not enough money. Money
#       refunded."
#   b. But if the user has inserted enough money, then the cost of the drink
#       gets added to the machine as the profit and this will be reflected
#       the next time "report" is triggered. E.g.
#       Water: 100ml
#       Milk: 50ml
#       Coffee: 76g
#       Money: $2.5
#   c. If the user has inserted too much money, the machine should offer
#       change. E.g. "Here is $2.45 dollars in change." The change should be
#       rounded to the nearest 2 decimal places.
# // TODO 7 - Make Coffee.
#   a. If the transaction is successful and there are enough resources to make
#       the drink the user selected, then the ingredients to make the drink
#       should be deducted from the coffee machine resources.
#
#       E.g. report before purchasing latte:
#       Water: 300ml
#       Milk: 200ml
#       Coffee: 100g
#       Money: $0
#
#       report after purchasing latte:
#       Water: 100ml
#       Milk: 50ml
#       Coffee: 76g
#       Money: $2.5
#   b. Once all resources have been deducted, tell the user
#       "Here is your latte ☕️. Enjoy!".
#       If latte was their choice of drink.
