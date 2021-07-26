# this challenge is to solve the hurdle 4 challenge at:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle4.json
# this is a game that already has some built-in functions and you use those to make more complex functions 
# to complete the challenges
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    wall_height = 0
    while wall_on_right() == True:
        move()
        wall_height += 1
    turn_right()
    move()
    turn_right()
    while wall_height > 0:
        move()
        wall_height -= 1
    turn_left()
while not at_goal():
    if not wall_in_front():
        move()
    else:
        jump()