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


screen.listen()
screen.onkey(key='space', fun=move_forwards)
screen.exitonclick()