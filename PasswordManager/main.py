from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

random_letters = [random.choice(letters) for letter in range(nr_letters)]
password_list += random_letters

random_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
password_list += random_symbols

random_numbers = [random.choice(numbers) for number in range(nr_numbers)]
password_list += random_numbers

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    username = email_username_input.get()
    password = password_input.get()

    # show error box if any field is left blank
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please don't leave any fields blank.")
    else:
        # confirm user entered info is correct:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\nUsername: {username}\n" +
                                               f"Password: {password}\nIs it ok to save?")
        if is_ok:
            # save user info
            entry = f"{website} | {username} | {password}\n"
            with open("data.txt", 'a') as data:
                data.write(entry)

            # clear input fields
            website_input.delete(0, END)
            password_input.delete(0, END)

            # reset focus
            website_input.focus()


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
