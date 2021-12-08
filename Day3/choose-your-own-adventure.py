print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

# Decision functions
def left_or_right(playing_game):
    '''Controls the first decision in the adventure.'''
    print("You are on a tiny beach that is surrounded by ridiculously high, un\
        scalable cliffs. After looking around for a while, you notice a large \
        crack at the base of one of the cliffs. You manage to wriggle your way\
        through. Once on the other side, you are surrounded by a lush jungle. \
        There is a path. You can venture left or right.")
playing_game = True
while playing_game:
    first_choice_is_valid = False

    first_choice = input("Which way do you want to go? Left or right? ")
    cleaned_first_choice = first_choice.lower()
    if cleaned_first_choice is not "left" and cleaned_first_choice is not "right":
        print("Sorry, that's not a valid choice. Please choose left or right.")

    if cleaned_first_choice == "left":
        print("You come to a small river. ")
    elif cleaned_first_choice == "right":
        print("You trip on a vine, stumble, and fall into a pit. Turns out to \
            be filled with poisonous snakes. So there's that. GAME OVER.")
        break
print("GAME OVER")
