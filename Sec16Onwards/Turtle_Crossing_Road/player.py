STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color("black")
        self.goto_start()
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish(self):
        if self.ycor()>280:
            return True
        else:
            return False

    def goto_start(self):
        self.goto(STARTING_POSITION)
