from tkinter import *


def button_clicked():
    print("I got clicked!")
    new_text = user_input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# you can add padding to components
window.config(padx=20, pady=20)

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=0, y=0)  # the .place() layout manager lets you specify an x and y value for placement of the
# component
# there is also a .grid() layout manager
my_label.grid(column=0, row=0)  # .grid() doesn't work without other components in the grid.
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me!", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# New Button
new_button = Button(text="New Button!", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
user_input = Entry(width=10)
# user_input.pack()
user_input.grid(column=3, row=2)

window.mainloop()
