from turtle import Turtle

import data


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.penup()
        self.color('white')
        self.goto(0, 265)
        self.display()
        self.hideturtle()

    def update_score(self):
        self.score += 1

    def display(self):
        self.clear()
        self.write(f"score :{self.score} High score :{self.high_score}", align='center', font=('Arial', 24, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_highscore(self.high_score)
        self.score = 0
        self.display()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align='center', font=('Arial', 24, 'normal'))
    def read_high_score(self):
        with open("data.txt") as data_hs:
            hs = int(data_hs.read())
        return hs

    def write_highscore(self, hs):
        with open("data.txt",mode="w") as data_hs:
            data_hs.write(f"{hs}")
