from turtle import Turtle, Screen
import random

is_race_running: False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Bettin' Time!",
                            prompt="Which turtle do you think is going to win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

x = -230
y = -100

for color_from_list in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_from_list)
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 50
    turtles.append(new_turtle)

if user_bet:
    is_race_running = True

while is_race_running:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_running = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()

# ideas for expansion
# add a start and finish line
# add lines for lanes
# add messages from an announcer during the race
#   "And now green is in the lead! How long will they keep their position?" etc.
# add sound effects
# make the game repeatable
# give the player money to bet with
# give the turtles odds of winning
# payouts for bets
# player can end the game whenever with a key press
# game ends when the player reaches 0 dollars
# messages about the player's winnings
#   "Holy cow! You just won a billion dollars on green! That has to be some kind of record." etc.
