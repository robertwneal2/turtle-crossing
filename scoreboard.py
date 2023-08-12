from turtle import Turtle
FONT = ("Arial", 24, "normal")
GAME_OVER_FONT = ("Arial", 40, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(5, 5)
        self.hideturtle()
        self.goto(-435, 525)
        self.level = 0
        self.display_level()

    def display_level(self):
        self.write(f'Level: {self.level}', False, 'center', FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.display_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', False, 'center', GAME_OVER_FONT)