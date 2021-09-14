from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.goto(0, 270)


    def score_point(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.write(f"Final Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
