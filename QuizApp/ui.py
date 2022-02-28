from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.score_text = Label(text=f"Score:", font=("Ariel", 20, "italic"))
        self.score_text.grid(row=0, column=1)
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.canvas = Canvas(height=250, width=300)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.canvas.create_text(150, 125, fill="white", font=("Ariel", 20, "italic"), text="Test Question")
        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command="", padx=20, pady=20)
        self.true_button.grid(row=2, column=0)
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command="", padx=20, pady=20)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
