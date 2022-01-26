from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.listen()
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

game_is_running = True
while game_is_running:
    time.sleep(.05)
    screen.update()
    ball.move()
    # collision with top of screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
#     collision with left or right edge of the screen
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.goto(0, 0)
        ball.bounce_x()

screen.exitonclick()
