from tkinter import *
import requests


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    response.raise_for_status()
    data = response.json()[0]
    quote = data["q"]
    author = data["a"]
    canvas.itemconfig(quote_text, text=f"{quote}\n\n{author}")


window = Tk()
window.title("Zen Quotes")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

zen_img = PhotoImage(file="zen.png")
kanye_button = Button(image=zen_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
