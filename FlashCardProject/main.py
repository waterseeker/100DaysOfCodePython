import random
from tkinter import *
from functions import get_word_list, get_random_word

BACKGROUND_COLOR = "#B1DDC6"

# UI SETUP
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
# Language text
language_text = canvas.create_text(
    400, 150,
    fill="black",
    font=("Ariel", 40, "italic"),
    text="Finnish")
# Word text
word_text = canvas.create_text(
    400, 263,
    fill="black",
    font=("Ariel", 40, "bold"),
    text="on")
incorrect_image = PhotoImage(file="images/wrong.png")
incorrect_button = Button(image=incorrect_image, highlightthickness=0)
incorrect_button.grid(row=1, column=0)
correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0)
correct_button.grid(row=1, column=1)

words_dict = get_word_list(50)
random_word_entry = get_random_word(words_dict)
print(random_word_entry)

window.mainloop()
