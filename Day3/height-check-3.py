print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride.")
    age = int(input("How old are you? "))
    if age < 12:
        print("Your ticket will be $5.")
    elif age < 19:
        print("Your ticket will be $7.")
    else:
        print("Your ticket will be $12.")
else:
    print("You can't ride.")
