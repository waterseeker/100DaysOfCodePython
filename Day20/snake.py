from turtle import Turtle
MOVE_DISTANCE = 20

class Snake():
    def __init__(self):
        self.x_coordinate = 0
        self.y_coordinate = 0
        self.snake_segments = []
        self.create_snake()

    def create_snake(self):
        for _ in range(3):
            snake_segment = Turtle(shape="square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(self.x_coordinate, self.y_coordinate)
            self.snake_segments.append(snake_segment)
            self.x_coordinate += -20

    def move(self):
        for segment_number in range(len(self.snake_segments) - 1, 0, -1):
            new_x_coordinate = self.snake_segments[segment_number - 1].xcor()
            new_y_coordinate = self.snake_segments[segment_number - 1].ycor()
            self.snake_segments[segment_number].goto(new_x_coordinate, new_y_coordinate)
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.snake_segments[0].setheading(90)

    def down(self):
        self.snake_segments[0].setheading(270)

    def left(self):
        self.snake_segments[0].setheading(180)

    def right(self):
        self.snake_segments[0].setheading(0)
