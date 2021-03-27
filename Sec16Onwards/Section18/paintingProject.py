# import colorgram
#
# colors = colorgram.extract('download.jpeg', 16)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)

import turtle as turtle_module
import random
color_list = [(57, 106, 148), (224, 200, 110), (133, 85, 59), (222, 141, 65), (195, 145, 171), (234, 225, 203), (144, 179, 203), (224, 233, 230), (138, 82, 106), (209, 91, 68), (134, 182, 136), (187, 79, 121), (69, 104, 89), (236, 222, 230), (65, 155, 89)]
turtle_module.colormode(255)
tim= turtle_module.Turtle()
tim.penup()
tim.setheading(230)
tim.forward(300)
tim.setheading(0)

def line():
    for _ in range(10):
        tim.dot(15, random.choice(color_list))
        tim.forward(50)


def rigth():
    tim.setheading(90)
    tim.penup()
    tim.forward(40)
    tim.setheading(180)
    tim.forward(50)

def left():
    tim.setheading(90)
    tim.penup()
    tim.forward(40)
    tim.setheading(0)
    tim.forward(50)

for i in range(5):
    line()
    rigth()
    line()
    left()

screen = turtle_module.Screen()
screen.exitonclick()
