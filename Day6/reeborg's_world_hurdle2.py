# this challenge is to solve the hurdle 2 challenge at:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
# this is a game that already has some built-in functions and you use those to make more complex functions 
# to complete the challenges
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
def move_and_jump():
    move()
    jump()
while at_goal() == False:
    move_and_jump()