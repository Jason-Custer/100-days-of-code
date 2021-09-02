import colorgram
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.speed(0)
timmy.hideturtle()

screen = Screen()
screen.colormode(255)

colors = colorgram.extract('hirst-spot-painting.jpg', 20)


def random_color():
    random_color = colors[random.randint(0, 19)]
    random_rgb = random_color.rgb
    return random_rgb


timmy.penup()
timmy.setposition(-275, -215)


for line in range(10):
    for number in range(10):
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
        timmy.dot(20, random_color())
        timmy.penup()
    timmy.left(90)
    timmy.forward(50)
    timmy.right(90)
    timmy.backward(500)

screen.exitonclick()
