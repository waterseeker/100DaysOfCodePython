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
# // TODO - print report of all coffee machine resources
# When the user enters “report” to the prompt, a report should be generated
# that showsthe current resource values.
# e.g.Water: 100mlMilk: 50mlCoffee: 76gMoney: $2.5