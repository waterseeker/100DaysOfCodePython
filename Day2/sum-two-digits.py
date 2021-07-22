## Data Types

# Instructions

# Write a program that adds the digits in a 2 digit number. 
# e.g. if the input was 35, then the output should be 3 + 5 = 8

while True:
    two_digit_number = input("Type a two digit number: ")
    if len(two_digit_number) != 2:
        print("Sorry, that's not a two digit number, please try again.")
        continue
    try:
        input_cast_to_int = int(two_digit_number)
        result = sum(int(digit) for digit in two_digit_number)
        print("The sum is " + str(result))
        break
    except ValueError:
        print("Sorry, that's not a two digit number.")
        continue