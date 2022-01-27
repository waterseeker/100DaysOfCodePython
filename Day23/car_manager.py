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
        super.__init__()
        self.hideturtle()
        self.penup()
        self.cars = []
        self.setposition(280, random.randint(-280, 280))

    def spawn_cars(self):
        for _ in range(random.randint(1, 5)):
            car = Turtle()
            car.color(random.choice(COLORS))
            car.penup()
            car.shape("square")
            car.setposition(280, random.randint(-280, 280))

    def move_cars(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)
            # TODO remove the car from the game when it goes off of the screen.
            # if car.xcor() < -280:

