# Modifying Global Scope
enemies = 1


def increase_local_enemies():
    # this is creating an entirely new variable, not referencing the global one
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_local_enemies()
print(f"enemies outside function: {enemies}")


def increase_global_enemies():
    global enemies
    enemies = 2
    print(f"Global enemies = {enemies}")


increase_global_enemies()
# but you shouldn't modify global variables like this. it's error-prone and
# considered bad practice in Python.
#
# Instead, you can use a return statement to modify the global variable


def increase_global_enemies_with_return():
    print(f"Global enemies = {enemies}")
    return enemies + 1


enemies = increase_global_enemies_with_return()
print(f"Global enemies = {enemies}")
