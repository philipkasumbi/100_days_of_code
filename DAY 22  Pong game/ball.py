from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move_diagonally(self):
        new_x = self.xcor()+20
        new_y = self.ycor() + 20
        self.goto(new_x,new_y)