# this challenge is to solve the maze challenge at:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# this is a game that already has some built-in functions and you use those to make more complex functions 
# to complete the challenges
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not is_facing_north():
    turn_left()
while not at_goal():
    if wall_on_right() and not wall_in_front():
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif not right_is_clear():
        turn_left()