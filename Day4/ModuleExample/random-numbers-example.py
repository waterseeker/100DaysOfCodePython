import random
import my_module

# example of using something from a module
# print(my_module.pi)

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

# random decimal in a range
random_decimal_between_zero_and_five = random.randint(0, 4) + random.random()
print(random_decimal_between_zero_and_five)
# or
another_way = random.random() * 5
print(another_way)
