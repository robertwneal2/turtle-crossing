import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1200, height=1200)
screen.tracer(0)
screen.title('Turtle Crossing')

player = Player()
screen.listen()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_left, 'Left')
screen.onkey(player.move_right, 'Right')

scoreboard = Scoreboard()
scoreboard.display_level()

car_manager = CarManager()
refresh = 1/60

game_is_on = True
while game_is_on:
    level_complete = False
    while not level_complete:
        time.sleep(refresh)
        car_manager.move_cars()
        screen.update()
        if player.is_finished():
            level_complete = True
            player.move_to_start()
            car_manager.level_up()
            scoreboard.next_level()
        elif car_manager.is_player_collision(player):
            level_complete = True
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
