from turtle import Turtle, Screen

# Challenge: draw a dashed line. solid for 10, empty for 10, repeat this 50
# times.
tim = Turtle()
tim.shape("turtle")
tim.color("forestgreen")
for _ in range(50):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()
