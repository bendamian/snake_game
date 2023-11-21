from turtle import Screen, Turtle

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")

square_list = []
x = 0
# TODO : Create a snake body
for i in range(3):
    new_square = Turtle()
    new_square.color("white")
    new_square.shape("square")
    new_square.goto(x, 0)
    square_list.append(new_square)
    x -= 20

screen.exitonclick()
