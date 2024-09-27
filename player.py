from turtle import Turtle
import random

COLOURS = ["red", "yellow", "blue", "black", "purple"]


class Player (Turtle):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        self.shape("turtle")
        self.penup()
        self.goto(0,-280)
        self.setheading(90)
        self.color(random.choice(COLOURS))

    def move(self):
        self.forward(15)

    def move_back(self):
        self.backward(15)

    def check(self):
        if self.ycor() > 295:
            return True
        else:
            return False

    def reposition(self):
        self.goto(0, -280)




