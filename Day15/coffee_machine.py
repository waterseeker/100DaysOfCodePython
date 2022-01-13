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


# testing code
choice = get_drink_choice()
drink = get_drink_item(choice)
print(drink['ingredients']["water"])
