from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 260)
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level : {self.score}", align="center", font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)