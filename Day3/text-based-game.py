# Make a text-based game using user input that will follow the branching
# logic at https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
choice_1 = input("You come to a branch in the path. Do you go left or right? ").lower()
if choice_1 == "left":
    choice_2 = input("You walk down the left path for a ways and come to a river. You think you might be able to swim across. Looking upstream you see a log floating down the river towards you. If you wait, you think you could grab ahold of it and use it to make a bridge. Do you swim or wait? ").lower()
    if choice_2 != "wait":
        print("You wade into the river. The water is cold but not unbearable. You make it about halfway across and suddenly feel something tugging at your feet. You fight as hard as you can but are eventually dragged down to your doom by the local trout. Game Over.")
    else:
        choice_3 = input("You bide your time, grab the log, and manage to secure one end of it on your side of the shore with some rocks. The other end is not quite on the opposite shore, but you manage to wedge it into some roots. You wait a couple of minutes to make sure it's going to hold and then carefully make your way across. Once you're safely on the other shore, you notice three doors.... that's odd. You're certain these weren't here before. There is a red one, a yellow one, and a blue one. Red, yellow, or blue? Which do you choose? ").lower()
        if choice_3 == "red":
            print("Red like fire. You open the door only to be blasted full-force by the flaming breath of a mildly infuriated dragon on the other side. The nerve. Game Over.")
        elif choice_3 == "blue":
            print("Blue like berries. You open the door and carefully peer through. There seems to be an entire forest on the other side of this door. You step through, amazed, only to be devoured by beasts lying in wait on the other side of the door. Game Over.")
        elif choice_3 == "yellow":
            print("You cautiously open the yellow door. There is a tavern on the other side, alive with the sounds of live music. You recognize the smell of spiced roasted potatoes and ale wafting through to your side of the doorway. Stepping through, you hear someone cheer 'Huzzah!!!' which is quickly followed by everyone in the tavern cheering the same thing while they life their mugs to toast you. They show you to a seat at the bar where there is a small treasure chest waiting for you. You Win!")
        else:
            print("Game Over.")
else:
    print("The ground give away beneath your feet. You scramble to grab onto something but fall into the earth. Game Over.")
