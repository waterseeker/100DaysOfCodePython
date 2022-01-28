from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# The turtle the player controls
# it moves forward when the player presses the "Up" arrow key
# it can only move forward


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.reset_position()
        self.setheading(90)

    def move_up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def reset_position(self):
        self.setposition(STARTING_POSITION)

    def is_collided_with(self, b):
        return abs(self.xcor() - b.xcor()) < 20 and abs(self.ycor() - b.ycor()) < 10
