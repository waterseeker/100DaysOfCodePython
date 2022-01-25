from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.listen()
screen.tracer(0)

player_1 = Paddle(-360, 0)
player_2 = Paddle(350, 0)

screen.onkey(player_1.move_up, "w")
screen.onkey(player_1.move_down, "s")
screen.onkey(player_2.move_up, "Up")
screen.onkey(player_2.move_down, "Down")

game_is_running = True
while game_is_running:
    screen.update()
    screen.exitonclick()