from turtle import Turtle

FONT = ("Courier", 24, "normal")


# displays the current level in the upper left of the screen f"Level: {level_number}"
#  and GAME OVER when the gams has ended.

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level_number = 0
        self.update_level()

    def update_level(self):
        self.clear()
        self.level_number += 1
        self.goto(-230, 260)
        self.write(f"Level: {self.level_number}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
