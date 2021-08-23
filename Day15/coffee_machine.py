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
