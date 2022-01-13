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
}


def get_drink_choice(supply_levels):
    """Gets user input to select a drink. Returns the drink item from the
    MENU. Returns False if user inputs 'off'"""
    drink_choice = input("What would you like? (espresso/latte/cappuccino):\n")
    cleaned_drink_choice = drink_choice.strip().lower()
    if cleaned_drink_choice == "off":
        return False
    elif cleaned_drink_choice == "report":
        # print out report of resource balances
        print(f"Water: {supply_levels['water']}ml")
        print(f"Milk: {supply_levels['milk']}ml")
        print(f"Coffee: {supply_levels['coffee']}g")
        print(f"Money: ${supply_levels.get('money', 0.00)}")
    elif cleaned_drink_choice not in MENU:
        print("Please select espresso, latte, or cappuccino.")
        return get_drink_choice()
    else:
        return cleaned_drink_choice


def get_drink_item(drink_name):
    """Takes in a string, returns item with that key from the MENU"""
    return MENU[drink_name]


def get_payment():
    """Asks the user for quarters, dimes, nickles, and pennies. Returns the
    total of coins given in cents."""
    getting_quarters = True
    while getting_quarters:
        try:
            number_of_quarters = int(input("how many quarters?: "))
            getting_quarters = False
        except ValueError:
            print("Please enter a number.")
            continue
    getting_dimes = True
    while getting_dimes:
        try:
            number_of_dimes = int(input("how many dimes?: "))
            getting_dimes = False
        except ValueError:
            print("Please enter a number.")
            continue
    getting_nickles = True
    while getting_nickles:
        try:
            number_of_nickles = int(input("how many nickles?: "))
            getting_nickles = False
        except ValueError:
            print("Please enter a number.")
            continue
    getting_pennies = True
    while getting_pennies:
        try:
            number_of_pennies = int(input("how many pennies?: "))
            getting_pennies = False
        except ValueError:
            print("Please enter a number.")
            continue
    total_cents = (number_of_quarters * 25 + number_of_dimes * 10 +
                   number_of_nickles * 5 + number_of_pennies)
    return total_cents / 100


def process_payment(menu_item_cost, payment_amount):
    """Takes in a menu item and payment amount. If the payment amount is
    higher than the cost of the menu item, it returns change. If the payment
    is not enough, it prints a statement saying money is refunded and returns
    False."""
    if payment_amount < menu_item_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif payment_amount == menu_item_cost:
        print("Thank you for using exact change.")
        return True

    else:
        change = payment_amount - menu_item_cost
        print(f"Here is ${change} in change.")
        return True


def serve_drink(menu_item_name):
    """Takes in a menu item name, prints a message to the console, serving the
    item"""
    print(f"Here is your {menu_item_name} ☕️. Enjoy!")


# testing code
while True:
    choice = get_drink_choice(resources)
    if not choice:
        continue
    drink = get_drink_item(choice)
    drink_cost = drink["cost"]
    # check that there are enough resources to make the drink
    print("Please insert coins.")
    payment = get_payment()
    is_enough_payment = process_payment(drink_cost, payment)
    if not is_enough_payment:
        continue
    # add money from sale to resources balance
    serve_drink(choice)
    # Starts loop again
