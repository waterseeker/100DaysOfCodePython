from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.color("white")
        self.shape("square")
        self.penup()
        self.resizemode("user")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.setposition(x, y)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
