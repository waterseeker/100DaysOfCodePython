import random
from tkinter import *
from functions import get_word_list, get_random_word
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/finnish_words.csv")
words_dict = get_word_list(3)
current_card = {}


def get_next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = get_random_word(words_dict)
    canvas.itemconfig(card_language, text="Finnish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Finnish"], fill="black")
    canvas.itemconfig(card_background, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_language, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_img)


def word_known():
    # remove the entry from the dictionary
    words_dict.remove(current_card)
    # create / overwrite words_to_learn.csv from the remaining words
    df = pd.DataFrame(words_dict)
    df.to_csv("data/words_to_learn.csv")
    # get a new card
    get_next_card()


# UI SETUP
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
# Language text
card_language = canvas.create_text(
    400, 150,
    fill="black",
    font=("Ariel", 40, "italic"),
    text="")

# Word text
card_word = canvas.create_text(
    400, 263,
    fill="black",
    font=("Ariel", 40, "bold"),
    text="")

incorrect_image = PhotoImage(file="images/wrong.png")
incorrect_button = Button(image=incorrect_image, highlightthickness=0, command=get_next_card)
incorrect_button.grid(row=1, column=0)
correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, command=word_known)
correct_button.grid(row=1, column=1)

get_next_card()
window.mainloop()
