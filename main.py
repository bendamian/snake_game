from glob import glob
from turtle import Screen, Turtle
from typing import List
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
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
    screen.update()
    time.sleep(0.1)
    for n in range(len(square_list) - 1, 0, -1):
        new_x = square_list[n-1].xcor()
        new_y = square_list[n-1].ycor()
        square_list[n].goto(new_x, new_y)
    square_list[0].forward(20)
    square_list[0].left(90)

    x = int(square_list[0].xcor())
    if x <= 225:
        continue
    game_is_on = False

screen.exitonclick()
