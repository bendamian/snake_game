from glob import glob
from turtle import Screen, Turtle
from typing import List

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
# TODO :creating  snake body
x = 0
square_list = []

for _ in range(3):
    new_square = Turtle()
    new_square.shape("square")
    new_square.color("white")
    new_square.penup()
    new_square.goto(x, 0)
    square_list.append(new_square)
    x -= 20
# TODO : make snake move
game_is_on = True

while game_is_on:
    for square in square_list:
        square.forward(10)
        x = int(square_list[0].xcor())
        if x > 550:
            game_is_on = False

screen.exitonclick()
