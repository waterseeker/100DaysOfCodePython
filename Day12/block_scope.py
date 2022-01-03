# There is no block scope in Python
# If you create a variable in an if statement like...
if 3 > 2:
    x = 3

# or basically any indented block of code, then it has the scope of it's
# block. i.e. the 'if' line in this example, which would be global scope
# so we have access to x here.

print(x)

# but if you enclose that block in a function...
# then the variable will only have local scope there


def some_function():
    if 3 > 2:
        y = 3


# so this will throw an error
print(y)

# A variable that's created inside a nested if block will also be in the
# global scope

if 3 > 2:
    if 1 < 12:
        z = 20
print(z)
