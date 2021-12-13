# Write your code below this row 👇

# first_number = 1
# last_number = 101
# answer = sum(x for x in range(first_number, last_number) if x % 2 == 0)
# print(f"The sum of all even numbers between {first_number} and \
# {last_number} is {answer}")

# A solution where the range is set by user input
print("Welcome to the even number addition calculator.")
print("This program will add all even numbers in a range.")
print("You input the starting number and the ending number.")
print("Then the program will print out the sum of all even numbers between \
those numbers.")
while True:
    first_number = "start"
    last_number = "end"
    while first_number == "start":
        try:
            first_number = int(input("What is the first number in the \
range?\n"))
        except ValueError:
            print("Sorry, that's not a number. Try again.")
            continue
    while last_number == "end":
        try:
            last_number = (int(input("What is the last number in the \
range?\n")))
        except ValueError:
            print("Sorry, that's not a number. Try again.")
            continue
    if first_number > last_number:
        print("Sorry, the first number in your range has to be less than the \
last one.")
        continue
    if first_number == last_number:
        print("Sorry, you can't use the same number for the beginning and \
end numbers in the range.")
        continue
    answer = sum(x for x in range(first_number, last_number + 1) if x % 2 == 0)
    print(f"The sum of all even numbers between {first_number} and \
{last_number} is {answer}.")
