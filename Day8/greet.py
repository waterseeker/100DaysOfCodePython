# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet():
    print("Line 1")
    print("Line 2")
    print("Line 3")


greet()

# Function that allows for input


def greet_with_name(name):
    print(f"Hello {name}.")


greet_with_name("Smitty")

# Functions with more than one input


def greet_with(name, location):
    print(f"Hi {name}.")
    print(f"How's the weather in {location}?")


greet_with("Smitty", "Somewhere")


# Call greet_with using keyword arguments instead of positional arguments.
greet_with(location="Somewhere", name="Smitty")
