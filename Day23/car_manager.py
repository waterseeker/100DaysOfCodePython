from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# generates all the random cars in the game
#  and moves them across the screen
# cars are randomly generated along the y-axis and move from the right edge of the screen to the left edge
#   make them despawn once they are past the left edge of the screen
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.cars = []
        self.setposition(280, random.randint(-250, 250))

    def spawn_car(self):
        car = Turtle()
        car.color(random.choice(COLORS))
        car.penup()
        car.shape("square")
        car.setposition(280, random.randint(-280, 280))
        car.setheading(180)
        car.turtlesize(stretch_len=3)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)
