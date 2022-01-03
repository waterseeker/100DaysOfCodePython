# ################## Scope ####################

# enemies = 1


# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")


# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local Scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)


# # This will throw an error because potion strength is only in the local scope
# # of the drink_potion method.
# print(potion_strength)

# Global Scope
player_health = 10


def drink_potion():
    potion_strength = 2
    print(player_health)


# The method has access to the player_health variable because it was declared
# in the global scope.
drink_potion()
