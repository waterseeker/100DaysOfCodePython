from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(
    file="logo.png")  # canvas.create_image expects a PhotoImage, so you have to load the png like this first
canvas.create_image(100, 100, image=logo)
canvas.pack()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window.mainloop()
