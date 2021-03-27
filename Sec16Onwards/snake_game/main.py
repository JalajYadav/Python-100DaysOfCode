from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

game_is_on = True
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # collision check with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    # collision check with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -285 or snake.head.ycor() > 280 or snake.head.ycor() < -285:
        food.refresh()
        score.reset()
        snake.reset()

    # detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<16:
            food.refresh()
            screen.reset()
            snake.reset()





screen.exitonclick()
