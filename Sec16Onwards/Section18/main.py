from turtle import Turtle, Screen
import random

screen = Screen()
timmy = Turtle()
timmy.shape("turtle")
timmy.color("chartreuse4")

screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
timmy.pensize(5)
timmy.speed("fastest")
for i in range(100):
    timmy.pencolor(random_color())
    timmy.forward(25)
    timmy.setheading(random.choice(directions))

Screen().exitonclick()
