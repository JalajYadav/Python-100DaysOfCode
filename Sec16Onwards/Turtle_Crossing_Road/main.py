import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
#timmy is the name of the turtle
timmy = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(timmy.move,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #detect colision
    for car in car_manager.all_cars:
        if car.distance(timmy) < 20:
            game_is_on = False
            scoreboard.game_over()
    #detect successful crossing
    if timmy.is_at_finish():
        timmy.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()

