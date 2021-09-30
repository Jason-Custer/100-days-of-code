from turtle import Turtle

ALIGNMENT = "center"
FONT_1 = ("Arial", 20, "normal")
FONT_2 = ("Arial", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.goto(0, 270)
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.reset_scoreboard()


    def score_point(self):
        self.clear()
        self.score += 1
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT_1)
        self.goto(0, 250)
        self.write(f"High Score: {self.high_score}", align=ALIGNMENT, font=FONT_2)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", "w") as data:
            data.write(f"{self.high_score}")
        self.score = 0


    def reset_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT_1)
        self.goto(0, 250)
        self.write(f"High Score: {self.high_score}", align=ALIGNMENT, font=FONT_2)
