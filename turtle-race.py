from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)

race_is_on = False
user1_bet = screen.textinput("Player 1: Place your bet!", "Enter the color of turtle you think is going to win the race: ")
user2_bet = screen.textinput("Player 2: Place your bet!", "Enter the color of turtle you think is going to win the race: ")

starting_position = [150, 100, 50, 0, -50, -100, -150]
colors = ["red", 'orange', "yellow", "green", "blue", "purple", "pink"]
all_turtles = []

for turtle_index in range(0, 7):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y=starting_position[turtle_index])
    all_turtles.append(tim)

if user1_bet and user2_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            pen = Turtle()
            pen.hideturtle()
            pen.penup()
            pen.goto(-175, 150)
            if winning_color == user1_bet:
                pen.write(f"Player 1 won! The {winning_color} turtle is the winner!", font=("Arial", 16, "bold"))
            elif winning_color == user2_bet:
                pen.write(f"Player 2 won! The {winning_color} turtle is the winner!", font=("Arial", 16, "bold"))
            else:
                pen.write(f"You both lose! The {winning_color} turtle is the winner!", font=("Arial", 16, "bold"))
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
