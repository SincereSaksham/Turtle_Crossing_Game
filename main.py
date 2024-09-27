import time
from turtle import Screen

import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

play = Player()
sb = Scoreboard()
car = car_manager.CarManager()

screen.listen()
screen.onkeypress(play.move, "Up")
screen.onkey(play.move, "w")

game_is_on = True
cars_on = True
count = 1
while game_is_on:
    screen.update()
    count += 1
    if count == 25:
        count = 0
        car.cars()
    car.move()
    time.sleep(0.1)

    if play.check():
        sb.increase_score()
        car.increment_speed()
        play.reposition()

    for vehicle in car.carlist:
        if vehicle.distance(play) < 25:
            game_is_on = False
            sb.game_over()

    cars_on = True

screen.exitonclick()
