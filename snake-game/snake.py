# Import
from turtle import Turtle

# Constant Variable should be ALL CAPS
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    # Everything in init is executed when Snake class is call, that's why create_snake is there but move is not
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_segment(i)

    def add_segment(self, i):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(i)
        self.segments.append(new_square)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Reminder: range(A,B) does not include B. So it will be until before B
        for i in range(len(self.segments) - 1, 0, -1):  # range(first, last, interval)
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def reset(self):
        for i in self.segments:
            i.goto(1000,1000)
        self.segments.clear() # To clear all segment
        self.create_snake()