# Simple Turtle Drawing using WASD commands

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def clear():
    tim.clear()
    tim.reset()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.setheading(tim.heading() + 10)


def turn_right():
    tim.setheading(tim.heading() - 10)


screen.listen()
screen.onkey(clear, "c")
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.exitonclick()
