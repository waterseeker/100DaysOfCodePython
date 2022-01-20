from turtle import Turtle, Screen, colormode
from random import randint
# Challenge draw a triangle, square, pentagon, hexagon, heptagon, octagon,
# nonagon, and decagon. Each side should be 100 in length and a random color.

# each shape has angles = 360/#of sides

tia = Turtle()
tia.shape("turtle")
colormode(255)

sides = 3
while sides <= 10:
    # random color
    tia.color(randint(0, 255), randint(0, 255), randint(0, 255))
    for _ in range(sides):
        degrees = 360/sides
        tia.forward(100)
        tia.right(degrees)
    sides += 1

screen = Screen()
screen.exitonclick()
