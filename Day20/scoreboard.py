from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.setposition(x=0, y=260)
        self.update_score()

    def increase_score(self):
        self.score += 1

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}', move=False, align='center', font=('Arial', 24, 'normal'))
