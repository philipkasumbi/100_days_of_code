from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0,210)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.update()