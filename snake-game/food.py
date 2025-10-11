# Import
from turtle import Turtle
import random

# Food class inherited Turtle class
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    # By separating goto into separated its own function, this way we can called it during initialization, and during if statement (from main.py)
    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))