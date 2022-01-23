from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# create a snake body that is 3 turtle objects, each 20 X 20 white squares
# the first one is at 0, 0.
# each other one is 20px to the left
x_coordinate = 0
y_coordinate = 0
snake_segments = []
for _ in range(3):
    snake_segment = Turtle(shape="square")
    snake_segment.color("white")
    snake_segment.penup()
    snake_segment.goto(x_coordinate, y_coordinate)
    snake_segments.append(snake_segment)
    x_coordinate += -20

game_is_running = True
while game_is_running:
    screen.update()
    time.sleep(0.1)

    for segment_number in range(len(snake_segments) - 1, 0, -1):
        new_x_coordinate = snake_segments[segment_number - 1].xcor()
        new_y_coordinate = snake_segments[segment_number - 1].ycor()
        snake_segments[segment_number].goto(new_x_coordinate, new_y_coordinate)
    snake_segments[0].forward(20)

screen.exitonclick()
