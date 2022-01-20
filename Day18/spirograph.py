import turtle as t
import random

# draw a number of circles, each with a radius and distance of 100
# make each circle a random color
# change the tilt of the circle by a little bit each time

leon = t.Turtle()
t.colormode(255)
leon.shape("turtle")
leon.speed("fastest")


def random_color():
    """Returns a tuple of 3 random ints from 0 to 255"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


facing = 0
for _ in range(50):
    leon.right(facing)
    leon.color(random_color())
    leon.circle(100)
    facing += 10
