from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(
    file="logo.png")  # canvas.create_image expects a PhotoImage, so you have to load the png like this first
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)
generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)

# columnspan= will let you make an element span more than one column
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window.mainloop()
