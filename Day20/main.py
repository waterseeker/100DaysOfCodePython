from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# initial snake body
x_coordinate = 0
y_coordinate = 0
snake_body = []
for _ in range(3):
    snake_segment = Turtle(shape="square")
    snake_segment.color("white")
    snake_segment.goto(x_coordinate, y_coordinate)
    snake_body.append(snake_segment)
    x_coordinate += -20














screen.exitonclick()

# create a snake body that is 3 turtle objects, each 20 X 20 white squares
# the first one is at 0, 0.
# each other one is 20px to the left