from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 265)
        self.display()
        self.hideturtle()

    def update_score(self):

        self.score += 1

    def display(self):
        self.clear()
        self.write(f"score :{self.score}", align='center', font=('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=('Arial', 24, 'normal'))

