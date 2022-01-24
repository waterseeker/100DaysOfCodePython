from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# create a snake body that is 3 turtle objects, each 20 X 20 white squares
# the first one is at 0, 0.
# each other one is 20px to the left

snake = Snake()

game_is_running = True
while game_is_running:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
