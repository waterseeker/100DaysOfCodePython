print("welcome to the game.")
wants_to_play_is_valid = False
while not wants_to_play_is_valid:
    wants_to_play = input("would you like to play? Please enter yes or no. ").lower()
    if wants_to_play != "yes" and wants_to_play != "no":
        print("invalid. please choose yes or no.")
        continue
    if wants_to_play == "no":
        wants_to_play_is_valid = True
        print("Ok. See you later.")
        break
    elif wants_to_play == "yes":
        wants_to_play_is_valid = True
        playing_game = True
        while playing_game:
            first_choice_is_valid = False
            while not first_choice_is_valid:
                first_choice = input("l or r?")
                if first_choice != "l" and first_choice != "r":
                    print("invalid, choose l or r.")
                    continue
                if first_choice == "l":
                    print("continue game")
                    break
                elif first_choice == "r":
                    print("wrong choice.")
                    playing_game = False
                    break
print("GAME OVER")
