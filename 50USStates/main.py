import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

# You can import an image as a turtle shape
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

df = pandas.read_csv("50_states.csv")
state_names_list = df.state.tolist()
correct_guesses = 0
answer_state = screen.textinput(title="Guess A State", prompt="What's another state's name?").title()
game_is_running = True


# monday_row = data[data.day == "Monday"]

def write_state_name_on_map(state_name, data_frame):
    state_row = data_frame[data_frame.state == state_name]
    state_x = float(state_row.x)
    state_y = float(state_row.y)
    state_name_turtle = turtle.Turtle()
    state_name_turtle.hideturtle()
    state_name_turtle.penup()
    state_name_turtle.goto(state_x, state_y)
    state_name_turtle.write(state_name)


if answer_state in state_names_list:
    correct_guesses += 1
    write_state_name_on_map(answer_state, df)
    # remove_correct_state(answer_state)

while game_is_running:
    answer_state = screen.textinput(title=f"{correct_guesses}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state in state_names_list:
        correct_guesses += 1
        write_state_name_on_map(answer_state, df)
        # remove_correct_state(answer_state)
    else:
        continue

# use the answer_state to check against the state names in the csv file
# clean the user input (csv file state names are in title case)
# see if it's in the state names
#   if so, print the state name on the map at the coordinates given in the csv file for that state
#   if not, nothing happens and the user input box pops up again
# in the title of the text input, keep track of the total number of correct guesses out of 50
#   "4/50 States Correct" for example
screen.exitonclick()
