from turtle import Screen,Turtle
from paddle import  Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=550)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((385,0))
l_paddle = Paddle((-390,0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_diagonally()

    # detect collision with wall
    if ball.ycor() > 255 or ball.ycor() < -255:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 360 or ball.distance(l_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_x()

screen.exitonclick()