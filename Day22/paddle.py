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
        self.turtlesize(stretch_wid=5)
        self.turtlesize(stretch_len=1)
        self.setposition(x, y)

    def move_up(self):
        current_position = self.position()
        current_x = current_position[0]
        current_y = current_position[1]
        new_y = current_y + 20
        self.goto(current_x, new_y)

    def move_down(self):
        current_position = self.position()
        current_x = current_position[0]
        current_y = current_position[1]
        new_y = current_y - 20
        self.goto(current_x, new_y)
