import random
from turtle import Turtle, Screen, colormode

colormode(255)


colors = [(234, 232, 227), (230, 233, 239), (239, 231, 235), (228, 235, 231), (199, 162, 100), (62, 91, 128), (140, 170, 192), (139, 90, 48), (219, 206, 119), (135, 27, 52), (32, 41, 67), (78, 16, 36), (149, 59, 85), (167, 154, 49), (187, 143, 162), (134, 183, 147), (46, 55, 100), (181, 95, 107), (56, 39, 27), (96, 118, 167), (80, 150, 159), (89, 152, 92), (71, 118, 93), (220, 175, 187), (169, 207, 163), (161, 202, 215), (192, 95, 74), (178, 187, 213), (46, 73, 75), (76, 69, 44)]



phil = Turtle()
phil.speed("fastest")
phil.penup()
phil.hideturtle()
phil.setx(-225)
phil.sety(-150)
phil.setheading(0)


number_of_dots = 10
spacing = 50

for row in range(number_of_dots):
    for col in range(number_of_dots):
        phil.dot(20, random.choice(colors))
        phil.forward(spacing)

    # move to next row
    phil.setx(-225)
    phil.sety(phil.ycor() + spacing)







screen = Screen()
screen.exitonclick()

