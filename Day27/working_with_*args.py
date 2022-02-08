# Challenge:
# Create a function called add that will take any number of arguments, add them all up, and return the sum


def add(*args):
    # *args is a tuple.
    # it allows you to have unlimited positional arguments
    # since it's a tuple, you can access an argument by index like...
    print(f"The second argument is: {args[1]}")
    return sum([num for num in args])


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
