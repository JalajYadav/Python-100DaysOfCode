from turtle import Turtle, Screen
from playsound import playsound
import random
import time
import concurrent.futures
# used realpython website to implement threading link: https://realpython.com/intro-to-python-threading/

def music():
    playsound('audio.mp3')
    quit()


def race_main():
    screen = Screen()
    screen.setup(width=500, height=400)
    is_race_on = False
    user_guess = screen.textinput(title="Make your Bet", prompt="Which turtle would win the race? enter a color")
    colors = ["red", "green", "blue", "orange", "yellow", "purple"]
    y_pos = [-70, -40, -10, 20, 50, 80]
    all_turtles = []
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_pos[turtle_index])
        all_turtles.append(new_turtle)

    if user_guess:
        is_race_on = True

    while is_race_on:

        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_guess:
                    print(f"You won! {winning_color} turtle won.")
                    quit()
                else:
                    print(f"You lost! {winning_color} turtle won.")
                    quit()

            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
    screen.exitonclick()


def step(i):
    if i == 0:
        time.sleep(1)
        music()
    else:
        race_main()


with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(step, range(2))
