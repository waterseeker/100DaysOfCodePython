def calculate(n, **kwargs):
    # **kwargs is a dictionary, so order doesn't really matter
    # you can access arguments in **kwargs like you would access something from a dictionary
    for key, value in kwargs.items():
        # you can loop through the dict to access values like this...
        print(f"Key: {key}, Value{value}")
    # you can also access the values by using the key like this...
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(f"Using positional and **kwargs.\nAnswer: {n}")


calculate(2, add=3, multiply=5)
