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


def get_drink_choice():
    """Gets user input to select a drink. Returns the drink item from the
    MENU. Returns False if user inputs 'off'"""
    drink_choice = input("What would you like? (espresso/latte/cappuccino):\n")
    cleaned_drink_choice = drink_choice.strip().lower()
    if cleaned_drink_choice == 'off':
        return False
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
    else:
        change = payment_amount - menu_item_cost
        print(f"Here is ${change} in change.")


# testing code
while True:
    choice = get_drink_choice()
    if not choice:
        break
    drink = get_drink_item(choice)
    drink_cost = drink["cost"]
    print("Please insert coins.")
    payment = get_payment()
    change = process_payment(drink_cost, payment)
    if not change:
        break
    # serve_drink()
    # Here is your espresso <coffee icon>. Enjoy!
    # Starts loop again
