from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.color("chartreuse4")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


timmy.speed("fastest")


def draw_circle(size_of_gap):
    for i in range(360 // size_of_gap):
        timmy.pencolor(random_color())
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + size_of_gap)


draw_circle(5)

screen.exitonclick()
