import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
car_manager = CarManager()
score = Scoreboard()


screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player)<30:
            game_is_on = False
            score.game_over()

    #crossed
    if player.finish():
        player.goto_start()
        score.increase_level()
        car_manager.level_up()





screen.exitonclick()
