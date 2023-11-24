from turtle import Screen, Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
Move_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            new_square = Turtle()
            new_square.shape("square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(position)
            self.segment.append(new_square)

    def snake_move(self):

        for n in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[n - 1].xcor()
            new_y = self.segment[n - 1].ycor()
            self.segment[n].goto(new_x, new_y)
        self.segment[0].forward(Move_DISTANCE)
