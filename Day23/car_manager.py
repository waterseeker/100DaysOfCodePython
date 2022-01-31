from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# generates all the random cars in the game
#  and moves them across the screen
# cars are randomly generated along the y-axis and move from the right edge of the screen to the left edge
#   make them despawn once they are past the left edge of the screen
class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.color(random.choice(COLORS))
            car.penup()
            car.shape("square")
            random_y_position = random.randint(-240, 240)
            car.goto(300, random_y_position)
            car.setheading(180)
            car.shapesize(stretch_len=2)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
