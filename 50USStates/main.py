import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

# You can import an image as a turtle shape
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

screen.exitonclick()
