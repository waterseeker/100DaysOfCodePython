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


# Game stage functions
def first_path_choice(playing_game):
    '''Controls the first decision in the adventure.'''

    print("You are on a tiny beach that is surrounded by ridiculously high, un\
scalable cliffs. After looking around for a while, you notice a large crack at\
the base of one of the cliffs. You manage to wriggle your way through. Once on\
the other side, you are surrounded by a lush jungle. There is a path. You can \
venture left or right.")
    choice = input("Which way do you want to go? Left or right? ")
    cleaned_choice = choice.lower().strip()
    while True:
        if cleaned_choice != "left" and cleaned_choice != "right":
            print("Sorry, that's not a valid choice. Please choose left or \
        right.")
            choice = input("Would you like to go left, or right? ")
            cleaned_choice = choice.lower().strip()
            continue
        if cleaned_choice == "left":
            print("You come to a small river. ")
            playing_game = True
            return playing_game
        elif cleaned_choice == "right":
            print("You trip on a vine, stumble, and fall into a pit. Turns out\
             to be filled with poisonous snakes. So there's that.")
            playing_game = False
            return playing_game


def second_path_choice(playing_game):
    '''Controls the second decision in the adventure.'''
    if not playing_game:
        return
    print("After following the left path for a while you arrive at a wide \
river. You can try to cross the river now, or make camp for the afternoon and \
try after a nap.")
    choice = input("Wait or cross? ")
    cleaned_choice = choice.lower().strip()
    while True:
        if cleaned_choice != "wait" and cleaned_choice != "cross":
            print(f"Huh? What is {cleaned_choice}? Please choose cross or \
        wait.")
            choice = input("Would you like to go cross or wait? ")
            cleaned_choice = choice.lower().strip()
            continue
        if cleaned_choice == "wait":
            print("You make camp and have a nice lunch of roasted potatoes and\
                    carrots with some rosemary and an apple you were delighted\
                    to find on a nearby tree. After you break camp, you make\
                    your way across the river and follow a path that leads\
                    along the shore.")
            playing_game = True
            return playing_game
        elif cleaned_choice == "cross":
            print("You begin making your way across only to be eaten alive by\
                    vicious river trout! Who would have guessed?")
            playing_game = False
            return playing_game


# Gameplay
playing_game = True
while playing_game:
    playing_game = first_path_choice(playing_game)
    playing_game = second_path_choice(playing_game)
print("GAME OVER")
