import turtle as t
import random
# move the turtle in increments of 10
# each move should be randomized to be up, down, left, or right.
# make the turtle move faster than normal
# make the lines the turtle draws thicker than normal
# make each moves line a random color
geoff = t.Turtle()
geoff.pensize(10)
geoff.speed(0)
t.colormode(255)


def random_color():
    """Returns a tuple of 3 random ints from 0 to 255"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def move_turtle(turtle, duration):
    for _ in range(duration):
        turtle.color(random_color())
        angles = [0, 90, 180, 270]
        turtle.right(random.choice(angles))
        turtle.forward(10)


move_turtle(geoff, 500)
screen = t.Screen()
screen.exitonclick()
