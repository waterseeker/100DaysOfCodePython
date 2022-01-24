from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.setposition(x=0, y=260)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
