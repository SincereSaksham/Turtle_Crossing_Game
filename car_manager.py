

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

import random
import time
import turtle


class CarManager:

    def __init__(self):
        self.carlist = []
        self.speed = 0
        self.car_number = 0
        self.cars()
        # so my confusion isthi self. carlist isnt working. the error show attribute error. but carlist defined above works perfectily well


    def cars(self):
        for i in range(random.randint(2+self.car_number,5+self.car_number)):
            cars = turtle.Turtle("square")
            cars.penup()
            cars.shapesize(stretch_len=3, stretch_wid=1)
            cars.color(random.choice(COLORS))
            cars.goto(random.randint(300, 350), random.randint(-270, 250))
            self.carlist.append(cars)

    def move(self):
        for carobj in self.carlist:
            carobj.goto(carobj.xcor() - (STARTING_MOVE_DISTANCE + self.speed), carobj.ycor())

    def increment_speed(self):
        self.speed += 5
        self.car_number += 1


