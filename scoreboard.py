import random
import turtle
FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.level = None
        self.timmy = None
        self.points =0
        self.level_points = 1
        self.score()

    def score(self):
        self.timmy = turtle.Turtle()
        self.timmy.hideturtle()
        self.timmy.penup()
        self.timmy.goto(-270, 250)
        self.timmy.write(self.points, align="left", font=FONT)

        self.level = turtle.Turtle()
        self.level.hideturtle()
        self.level.penup()
        self.level.goto(270, 250)
        self.level.write(f"Level : {self.level_points}" , align="right", font=FONT)

    def increase_score(self):
        self.points += 5
        self.level_points += 1
        self.timmy.clear()
        self.level.clear()
        self.timmy.write(self.points, align = "left", font= FONT)
        self.level.write(f"Level : {self.level_points}", align= "right", font=FONT)

    def game_over(self):
        self.timmy.goto(0,0)
        self.timmy.write("Game Over", align="center", font= FONT)

