from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-270, 250)
        self.update_level()

    def update_level(self):
        self.write(f"Level:{self.level}", align="left", font=("Courier", 18, "normal"))

    def score_increase(self):
        self.clear()
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)