from tkinter import *


def button_clicked():
    print("I got clicked!")
    new_text = user_input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.pack()

# Button
button = Button(text="Click Me!", command=button_clicked)
button.pack()

# Entry
user_input = Entry(width=10)
user_input.pack()

window.mainloop()
