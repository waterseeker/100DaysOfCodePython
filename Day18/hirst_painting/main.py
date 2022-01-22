import colorgram
import turtle as t
import random

# colors = colorgram.extract('./hirst_loyalty.jpeg', 30)
#
# rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
# print(rgb_colors)

color_list = [(191, 218, 235), (238, 209, 223), (193, 140, 161), (60, 30, 39), (133, 73, 94), (231, 222, 209),
              (53, 39, 31), (116, 94, 70), (182, 96, 128), (175, 160, 136), (146, 177, 197), (206, 229, 215),
              (113, 37, 55), (224, 172, 190), (141, 177, 144), (70, 123, 87), (71, 89, 123), (128, 150, 71),
              (148, 208, 225), (33, 39, 53), (86, 155, 99), (30, 45, 33), (98, 47, 42), (166, 209, 183), (179, 101, 92),
              (181, 187, 214), (196, 203, 158), (219, 178, 173), (42, 57, 107), (72, 74, 37)]

# Challenge - use Turtle and the color list to create a spot painting
# the painting should be 10 by 10 spots
# each dot should be 20 in size and spaced apart by 50 paces
# TODO refactor code to use the changed start point
painter = t.Turtle()
painter.hideturtle()
painter.speed("fastest")
t.colormode(255)
# changing the start point to make the finished painting more centered
painter.setheading(225)
painter.penup()
painter.forward(250)
painter.setheading(0)
y_coordinate = -176.78
for _ in range(10):
    for _ in range (10):
        dot_color = random.choice(color_list)
        painter.dot(20, dot_color)
        painter.penup()
        painter.forward(50)
    y_coordinate += 50
    painter.goto(-176.78, y_coordinate)

screen = t.Screen()
screen.exitonclick()
