import time
import random
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

current_number_of_cars = 0
FINISH_LINE_Y_COR = 250
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
finish_line = Turtle()
finish_line.penup()
finish_line.goto(+300, FINISH_LINE_Y_COR)
finish_line.pendown()
finish_line.goto(-300, FINISH_LINE_Y_COR)
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    if player.ycor() == FINISH_LINE_Y_COR:
        player.reset_position()
        scoreboard.update_level()
    maximum_number_of_cars = scoreboard.level_number + 9
    if current_number_of_cars < maximum_number_of_cars:
        for _ in range(maximum_number_of_cars - current_number_of_cars):
            car_manager.spawn_car()
            current_number_of_cars += 1
            wait_interval = round(random.uniform(0.05, 2.00), 2)
            time.sleep(wait_interval)
    car_manager.move_cars()
    for car in car_manager.cars:
        if player.is_collided_with(car):
            game_is_on = False
            scoreboard.game_over()
            break
        if car.xcor() < -280:
            car_manager.cars.remove(car)
            car.clear()
            car.hideturtle()
            del car
            car_manager.spawn_car()
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
