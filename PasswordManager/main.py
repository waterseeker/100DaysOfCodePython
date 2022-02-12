from tkinter import *

user_data = []


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    global user_data
    website = website_input.get()
    username = email_username_input.get()
    password = password_input.get()

    # save user info
    user_data.append(f"{website} | {username} | {password}\n")
    with open("data.txt", 'w') as data:
        for line in user_data:
            data.write(line)
    # clear input fields
    website_input.delete(0, END)
    email_username_input.delete(0, END)
    password_input.delete(0, END)
    # reset focus and repopulate email
    website_input.focus()
    email_username_input.insert(0, "test@test.com")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(
    file="logo.png")  # canvas.create_image expects a PhotoImage, so you have to load the png like this first
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)  # columnspan will let you make an element span more than 1 column
website_input.focus()  # sets the cursor to be here when the app launches

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "test@test.com")  # .insert() lets you set an initial value in the field.

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)
generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
