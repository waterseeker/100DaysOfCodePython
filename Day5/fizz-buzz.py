# Write your code below this row 👇

# for num in range(1, 101):
#     if num % 15 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

# using user input


def go_again():
    '''Asks user if they want to run the program again and restarts
       the program if they do. Otherwise returns True'''
    choice = input("Run the program again? Y or N.\n").lower()
    if choice == "n":
        return
    else:
        return True


print("Welcome to the Fizz Buzz calculator.")
print("This program will ask you for a range of numbers.")
print("You input the starting number and the ending number.")
print("Then the program will ask you for a first and second divisor.")
print("Then for each number in the range, it will print 'Fizz' if the \
number is evenly divisible by the first divisor, 'Buzz' if it is evenly \
divisible by the second divisor and 'FizzBuzz' if it is evenly divisible \
by both.")
while True:
    start_range = "start"
    end_range = "end"
    first_divisor = "first divisor"
    second_divisor = "second divisor"
    while start_range == "start":
        try:
            start_range = int(input("What's the beginning of your range?\n"))
        except ValueError:
            print("Sorry, that's not a number. Try again.")
            continue
    while end_range == "end":
        try:
            end_range = (int(input("What is the end of your range?\n")))
        except ValueError:
            print("Sorry, that's not a number. Try again.")
            continue
    while first_divisor == "first divisor":
        try:
            first_divisor = int(input("What's the first divisor?\n"))
        except ValueError:
            print("Sorry, that's not a number. Try again.")
            continue
    while second_divisor == "second divisor":
        try:
            second_divisor = int(input("What's the second divisor?\n"))
        except ValueError:
            print("Sorry, that's not a number. Try again.")
            continue
    if start_range > end_range:
        print("Sorry, the first number in your range has to be less than the \
last one.")
        continue
    if start_range == end_range:
        print("Sorry, you can't use the same number for the beginning and \
end numbers in the range.")
        continue

    combo_divisor = first_divisor * second_divisor
    for num in range(start_range, end_range + 1):
        if num % combo_divisor == 0:
            print("FizzBuzz")
        elif num % first_divisor == 0:
            print("Fizz")
        elif num % second_divisor == 0:
            print("Buzz")
        else:
            print(num)

    run_again = go_again()
    if run_again:
        continue
    else:
        break
