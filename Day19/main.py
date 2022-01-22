import turtle
from turtle import Turtle, Screen

# CHALLENGE:
# create a turtle that will allow you to:
#   press the w key to go forwards
#             s key to go backwards
#             a key to go left
#             d key to go right
#             c key to clear the drawing and put the turtle back in the center
bella = Turtle()
screen = Screen()


def move_forwards():
    bella.forward(10)


def move_backwards():
    bella.backward(10)


def turn_left():
    bella.left(10)


def turn_right():
    bella.right(10)


def reset():
    bella.clear()
    bella.reset()


screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='a', fun=move_backwards)
screen.onkey(key='s', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=reset)

screen.exitonclick()
