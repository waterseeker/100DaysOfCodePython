from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✅"
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(
    file="tomato.png")  # canvas.create_image expects a PhotoImage, so you have to load the png like this first
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)

canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# you set the color of a label by using fg=blah instead of bg=blah
# "Timer" label at column 1, row 0
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 45), bg=YELLOW)
timer_label.grid(column=1, row=0)
# tomato is at column 1, row 1
# Start button is at column 0, row 2
# Reset button is at column 2, row 2
# Checkmarks label is at column 1, row 3
window.mainloop()
