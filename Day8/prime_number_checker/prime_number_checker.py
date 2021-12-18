# Write your code below this line 👇


def prime_checker(number):
    if number < 2:
        print("It's a prime number.")
        return
    divisor = 3
    while divisor * divisor <= n:
        if number % divisor == 0 and divisor != number:
            print("It's not a prime number.")
            return
        divisor += 1
    if number % number == 0:
        print("It's a prime number.")
# Write your code above this line 👆


# Do NOT change any of the code below👇
n = int(input("Check this number"))
prime_checker(number=n)
