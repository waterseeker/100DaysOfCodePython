playing_game = True
while playing_game:
    choice = input("l or r?")
    if choice is not "l" and choice is not "r":
        print("invalid, choose l or r.")
        # return to beginning of loop
    if choice == "l":
        print("continue game")
    elif choice == "r":
        print("wrong choice.")
        playing_game = False
        break
print("GAME OVER")