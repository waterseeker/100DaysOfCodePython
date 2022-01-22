from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Bettin' Time!",
                            prompt="Which turtle do you think is going to win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
# tian = Turtle(shape="turtle")
# tian.penup()
# tian.goto(x=-230, y=-100)

x = -230
y = -100

for color_from_list in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color_from_list)
    turtle.penup()
    turtle.goto(x, y)
    y += 50

screen.exitonclick()
