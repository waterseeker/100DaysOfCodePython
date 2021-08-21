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

coffee_emoji = '☕'


# // TODO 1 - Prompt user by asking
#   "What would you like? (espresso/latte/cappuccino)"
#   a. Check the user's input to decide what to do next.
#   b. The prompt should show every time action has completed, e.g. once the
#       drink is dispensed. The prompt should show again to serve the next
#       customer.
# // TODO 2 - Turn off the Coffee Machine by entering "off" to the prompt.
#   a. For maintainers of the coffee machine, they can use "off" as the secret
#       word to turn off the machine. Your code should end execution when this
#       happens.
# // TODO 3 - Print report.
#   a. When the user enters "report" to the prompt, a report should be
#       generated that shows the current resource values e.g.
#       Water: 100ml
#       Milk: 50ml
#       Coffee: 76g
#       Money: $2.5
# // TODO 4 - Check resources sufficient?
#   a. When the user chooses a drink, the program should check if there are
#       enough resources to make that drink.
#   b. E.g. if Latte requires 200ml water but there is only 100ml left
#       in the machine, it should not continue to make the drink but
#       print "Sorry there is not enough water."
#   c. The same should happen if another resource is depleted,
#       e.g. milk or coffee.
