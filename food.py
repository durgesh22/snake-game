import random
from turtle import Turtle
from random import Random


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shapesize(.5, .5)
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x: int = random.randint(-280, 280)
        random_y: int = random.randint(-280, 280)
        self.goto(random_x,random_y)

