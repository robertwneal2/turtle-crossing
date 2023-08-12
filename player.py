from turtle import Turtle

STARTING_POSITION = (0, -575)
MOVE_DISTANCE = 25
FINISH_LINE_Y = 575


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.shapesize(2, 2)
        self.penup()
        self.speed(0)
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.fd(MOVE_DISTANCE)

    def move_left(self):
        current_y = self.ycor()
        new_x = self.xcor() - MOVE_DISTANCE
        if new_x > -550:
            self.goto(new_x, current_y)

    def move_right(self):
        current_y = self.ycor()
        new_x = self.xcor() + MOVE_DISTANCE
        if new_x < 550:
            self.goto(new_x, current_y)

    def move_to_start(self):
        self.goto(STARTING_POSITION)

    def is_finished(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
