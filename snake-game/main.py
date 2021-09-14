from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Pro")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.right,"Right")
screen.onkeypress(snake.left,"Left")

game_over = False

while not game_over:
    screen.update()
    time.sleep(.1)

    snake.move()

    # Detect when food is eaten and grow snake:
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_point()
        snake.extend()

    # Detect collision with wall:
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_over = True
        scoreboard.game_over()

    # Detect collision with tail:
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_over = True
            scoreboard.game_over()

screen.exitonclick()
