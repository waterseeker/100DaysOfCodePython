## Prime Numbers

# Instructions

# Prime numbers are numbers that can only be cleanly divided by itself and 1. 
# https://en.wikipedia.org/wiki/Prime_number

# **You need to write a function** that checks whether if the number passed into 
# it is a prime number or not.

# e.g. 2 is a prime number because it's only divisible by 1 and 2.

# But 4 is not a prime number because you can divide it by 1, 2 or 4.
# (https://cdn.fs.teachablecdn.com/s0gceS97QD6MP5RUT49H)

# Here are the numbers up to 100, prime numbers are highlighted in yellow:
# (https://cdn.fs.teachablecdn.com/NZqVclSt2qAe8KhTsUtw)

# Example Input 1
# 73

# Example Output 1
# It's a prime number.

# Example Input 2
# 75

# Example Output 2
# It's not a prime number.

# Hint

# 1. Remember the modulus: 

# https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python

# 2. Make sure you name your function/parameters the same as when it's called 
# on the last line of code. 

# 3. Use the same wording as the Example Outputs to make sure the tests pass.
#Write your code below this line 👇
def prime_checker(number):
    isprime = True
    if number < 2 or number % 2 == 0:
        isprime = False
    if number % 3 == 0:
        isprime = False
    square_root_of_number = int(n**0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6.
    f = 5
    while f <= square_root_of_number:
        if number % f == 0:
            isprime = False
        if number % (f + 2) == 0:
            isprime = False
        f += 6
    if isprime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

# logic from 
# https://stackoverflow.com/questions/15285534/isprime-function-for-python-language/15285588
