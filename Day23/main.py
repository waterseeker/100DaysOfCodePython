import time
import random
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# TODO make at least X space between car spawns
# increase number of cars when level increases
# spread out car spawns more so they're not mostly a single line of cars all starting at the same time.
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
        car_manager.level_up()
        player.reset_position()
        scoreboard.update_level()
    car_manager.spawn_car()
    car_manager.move_cars()
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
        if car.xcor() < -280:
            car_manager.cars.remove(car)
            car.clear()
            car.hideturtle()
            del car
            car_manager.spawn_car()
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
