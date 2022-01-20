from turtle import Turtle, Screen, colormode
from random import randint, choice
# move the turtle in increments of 10
# each move should be randomized to be up, down, left, or right.
# make the turtle move faster than normal
# make the lines the turtle draws thicker than normal
# make each moves line a random color
geoff = Turtle()
geoff.pensize(3)
geoff.speed(0)
colormode(255)


def move_turtle(turtle, duration):
    for _ in range(duration):
        turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
        angles = [0, 90, 180, 270]
        turtle.right(choice(angles))
        turtle.forward(10)


move_turtle(geoff, 500)
screen = Screen()
screen.exitonclick()
