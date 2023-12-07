from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
Move_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def snake_move(self):

        for n in range(len(self.segment) - 1, 0, -1):
            #
            new_x = self.segment[n - 1].xcor()
            new_y = self.segment[n - 1].ycor()
            self.segment[n].goto(new_x, new_y)
        self.head.forward(Move_DISTANCE)

    def add_segment(self, position):
        new_square = Turtle()
        new_square.shape("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.segment.append(new_square)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def extent(self):
        # add a new segment to snake
        self.add_segment(self.segment[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

