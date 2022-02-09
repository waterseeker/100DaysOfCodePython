from tkinter import *

window = Tk()
window.title = "Miles to Km Converter"
window.minsize(width=200, height=150)
window.config(padx=20, pady=20)


def miles_to_kilometers():
    miles = user_input.get()
    kilometers = int(miles) * 1.6
    rounded_kilometers = round(kilometers, 2)
    output_label.config(text=rounded_kilometers)


user_input = Entry(width=10)
user_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

output_label = Label(text=0)
output_label.grid(column=1, row=1)

kilometers_label = Label(text="Km")
kilometers_label.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_kilometers)
button.grid(column=1, row=2)

window.mainloop()
