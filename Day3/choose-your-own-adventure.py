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
    '''Game logic for the first decision in the adventure.'''

    print("You are on a tiny beach that is surrounded by ridiculously high, \
unscalable cliffs. After looking around for a while, you notice a large \
crack at the base of one of the cliffs. You manage to wriggle your way \
through. Once on the other side, you are surrounded by a lush jungle. There \
is a path. You can venture left or right.")
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
            print("You trip on a vine, stumble, and fall into a pit. Turns \
        out to be filled with poisonous snakes. So there's that.")
            playing_game = False
            return playing_game


def second_path_choice(playing_game):
    '''Game logic for the second decision in the adventure.'''
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
            print("You make camp and have a nice lunch of roasted potatoes \
        and carrots with some rosemary and an apple you were delighted to \
        find on a nearby tree. After you break camp, you make your way \
        across the river and follow a path that leads along the shore.")
            playing_game = True
            return playing_game
        elif cleaned_choice == "cross":
            print("You begin making your way across only to be eaten alive by \
                    vicious river trout! Who would have guessed?")
            playing_game = False
            return playing_game


def third_path_choice(playing_game):
    '''Game logic for the third decision in the adventure.'''
    if not playing_game:
        return
    print("You begin making your way along the shoreline towards a wall you \
can see in the distance. You set your sights on the wall and begin making \
your way there. After only a few steps, you hear an alarming noise coming \
from the river. Turning to look, you see the water frothing and foaming with \
what must be hundreds of fish thrashing on the surface. Must be those \
ravenous river trout you've heard so much about. Luck they didn't get you... \
this time. You turn back around and after about a hour or so you reach an \
old stone wall with three doors. One red, one yellow, one blue.")
    choice = input("Which door strikes your fancy? Red, yellow, or blue? ")
    cleaned_choice = choice.lower().strip()
    while True:
        if (cleaned_choice != "red" and cleaned_choice != "yellow" and
                cleaned_choice != "blue"):
            print(f"Sorry? There's no {cleaned_choice} door. Are you feeling \
        ok? Please choose red, yellow, or blue.")
            choice = input("Which one? Red, yellow, or blue? ")
            cleaned_choice = choice.lower().strip()
            continue
        if cleaned_choice == "red":
            print("You reach for the red door but before you can even touch \
        it you burst into flames. Ouch. That's like, lethal.")
            playing_game = False
            return playing_game
        elif cleaned_choice == "blue":
            print("My my, that is a very soothing shade of blue if I do say \
        so myself. That'll help distract you while you are being eaten alive \
        by the pack of wolves that just snuck up on you. Womp womp. More \
        like chomp, chomp. Amirite?")
            playing_game = False
            return playing_game
        elif cleaned_choice == "yellow":
            print("Ah yes, the color of cowards. When did that become a \
        thing anyway? I mean, lions are yellow. More of a yellowish brown \
        though really... oh sorry. Good choice on your part! You open the \
        yellow door and find glory and riches beyond measure. You win!")
            playing_game = False
            return playing_game


# Gameplay
playing_game = True
while playing_game:
    playing_game = first_path_choice(playing_game)
    if not playing_game:
        break
    playing_game = second_path_choice(playing_game)
    if not playing_game:
        break
    playing_game = third_path_choice(playing_game)
    if not playing_game:
        break
print("GAME OVER")
