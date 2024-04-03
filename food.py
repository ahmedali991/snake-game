#! /sur/bin/env python3
# ### This file contains the Food class ###
import random
from turtle import Turtle
#i need to inherit from the Turtle class

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape = Turtle("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)