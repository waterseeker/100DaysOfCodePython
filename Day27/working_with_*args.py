# Challenge:
# Create a function called add that will take any number of arguments, add them all up, and return the sum


def add(*args):
    return sum([num for num in args])


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
