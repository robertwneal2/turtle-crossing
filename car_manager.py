from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_SPEED = 2
MOVE_INCREMENT = 0.5
CAR_WIDTH = 5
CAR_HEIGHT = 2
CAR_X_START = 650
CAR_Y_RANGE_START = -500
CAR_Y_RANGE_END = 500
CAR_Y_RANGE_INC = 50
CAR_X_RANGE_START = -600
CAR_X_RANGE_END = 600
NUM_CARS = 15
COLLISION_X_OFFSET = 70
COLLISION_Y_OFFSET = 50


class CarManager:

    def __init__(self):
        self.cars = []
        self.populate_cars()
        self.car_speed = STARTING_SPEED

    def populate_cars(self):
        for i in range(NUM_CARS):
            rand_car_y = random.randrange(CAR_Y_RANGE_START, CAR_Y_RANGE_END, CAR_Y_RANGE_INC)
            rand_car_x = random.randint(CAR_X_RANGE_START, CAR_X_RANGE_END)
            pos = (rand_car_x, rand_car_y)
            self.create_car(pos)

    def is_player_collision(self, player):
        player_x = player.xcor()
        player_y = player.ycor()
        for car in self.cars:
            car_x = car.xcor()
            car_y = car.ycor()
            if (car_x - COLLISION_X_OFFSET < player_x < car_x + COLLISION_X_OFFSET
                    and car_y - COLLISION_Y_OFFSET < player_y < car_y + COLLISION_Y_OFFSET):
                return True
        return False

    def move_cars(self):
        for car in self.cars:
            car_x = car.xcor()
            car_y = car.ycor()
            car_x -= self.car_speed
            car.goto(car_x, car_y)
        self.reset_cars()

    def reset_cars(self):
        for car in self.cars:
            if car.xcor() <= -650:
                new_y = random.randrange(CAR_Y_RANGE_START, CAR_Y_RANGE_END, CAR_Y_RANGE_INC)
                car.goto(CAR_X_START, new_y)
            while self.is_car_interference(car):
                new_y = random.randrange(CAR_Y_RANGE_START, CAR_Y_RANGE_END, CAR_Y_RANGE_INC)
                pos = (CAR_X_START, new_y)
                car.goto(pos)

    def create_car(self, pos):
        car = Turtle()
        self.cars.append(car)
        car.penup()
        car.speed(0)
        car.shape('square')
        car.shapesize(CAR_HEIGHT, CAR_WIDTH)
        car.color(random.choice(COLORS))
        car.goto(pos)
        while self.is_car_interference(car):
            rand_car_y = random.randrange(CAR_Y_RANGE_START, CAR_Y_RANGE_END, CAR_Y_RANGE_INC)
            rand_car_x = random.randint(CAR_X_RANGE_START, CAR_X_RANGE_END)
            pos = (rand_car_x, rand_car_y)
            car.goto(pos)

    def is_car_interference(self, car_input):
        car_input_y = car_input.ycor()
        for car in self.cars:
            car_y = car.ycor()
            if car != car_input and car_y == car_input_y:
                if car_input.distance(car) < 125:
                    return True
        return False

    def level_up(self):
        rand_car_y = random.randrange(CAR_Y_RANGE_START, CAR_Y_RANGE_END, CAR_Y_RANGE_INC)
        pos = (CAR_X_START, rand_car_y)
        self.create_car(pos)
        self.car_speed += MOVE_INCREMENT
