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


def write_state_name_on_map(state_name, data_frame):
    state_row = data_frame[data_frame.state == state_name]
    state_x = float(state_row.x)
    state_y = float(state_row.y)
    state_name_turtle = turtle.Turtle(visible=False)
    state_name_turtle.hideturtle()
    state_name_turtle.penup()
    state_name_turtle.goto(state_x, state_y)
    state_name_turtle.write(state_name)


def remove_correct_state(state_name):
    state_names_list.remove(state_name)


def is_game_over():
    if len(state_names_list) == 0:
        return True
    return False


if answer_state in state_names_list:
    correct_guesses += 1
    write_state_name_on_map(answer_state, df)
    remove_correct_state(answer_state)

while game_is_running:
    if len(state_names_list) == 0:
        game_is_running = False
        continue
    answer_state = screen.textinput(title=f"{correct_guesses}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state in state_names_list:
        correct_guesses += 1
        write_state_name_on_map(answer_state, df)
        remove_correct_state(answer_state)
    if answer_state == "Exit":
        state_name_dict = {"state": state_names_list}
        df = pandas.DataFrame(state_name_dict)
        df.to_csv("states_to_learn.csv")
        game_is_running = False
