from turtle import Turtle,Screen
import  random

screen = Screen()
user_guess = screen.textinput("Make your bet","Who will win the race? Enter a color: ")

turtleracer1= Turtle()
turtleracer2= Turtle()
turtleracer3= Turtle()
turtleracer4= Turtle()
turtleracer5= Turtle()
turtleracer6= Turtle()

turtleracer1.shape("turtle")
turtleracer1.color("red")
turtleracer1.penup()
turtleracer1.goto(-250,-100)


turtleracer2.shape("turtle")
turtleracer2.color("green")
turtleracer2.penup()
turtleracer2.goto(-250,-60)


turtleracer3.shape("turtle")
turtleracer3.color("blue")
turtleracer3.penup()
turtleracer3.goto(-250,-20)


turtleracer4.shape("turtle")
turtleracer4.color("yellow")
turtleracer4.penup()
turtleracer4.goto(-250,20)


turtleracer5.shape("turtle")
turtleracer5.color("violet")
turtleracer5.penup()
turtleracer5.goto(-250,60)


turtleracer6.shape("turtle")
turtleracer6.color("indigo")
turtleracer6.penup()
turtleracer6.goto(-250,100)


finish_line = 245

for _ in range(250):
    turtleracer1.forward(random.randint(1, 10))
    if turtleracer1.xcor() >= finish_line:
        if user_guess == "red":
            print("You won the bet")
            break
        else:
            print("You lose to Turtle 1")
            break
    turtleracer2.forward(random.randint(1, 10))
    if turtleracer2.xcor() >= finish_line:
        if user_guess == "green":
            print("You won the bet")
            break
        else:
            print("You lose to Turtle 2")
            break
    turtleracer3.forward(random.randint(1, 10))
    if turtleracer3.xcor() >= finish_line:
        if user_guess == "blue":
            print("You won the bet")
            break
        else:
            print("You lose to Turtle 3")
            break
    turtleracer4.forward(random.randint(1, 10))
    if turtleracer4.xcor() >= finish_line:
        if user_guess == "yellow":
            print("You won the bet")
            break
        else:
            print("You lose to Turtle 4")
            break
    turtleracer5.forward(random.randint(1, 10))
    if turtleracer5.xcor() >= finish_line:
        if user_guess == "violet":
            print("You won the bet")
            break
        else:
            print("You lose to Turtle 5")
            break
    turtleracer6.forward(random.randint(1, 10))
    if turtleracer6.xcor() >= finish_line:
        if user_guess == "indigo":
            print("You won the bet")
            break
        else:
            print("You lose to Turtle 6")
            break
screen.exitonclick()