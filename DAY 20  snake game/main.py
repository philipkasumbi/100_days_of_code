from turtle import Turtle,Screen
import time

starting_point = [(0,0),(-20,0),(-40,0)]


screen = Screen()
screen.title("Snake Body Example")
screen.bgcolor("black")
screen.tracer(0)
screen.setup(width=500, height=500)

segments = []

for position  in starting_point:
    snake = Turtle("square")
    snake.color("white")
    snake.penup()
    snake.speed("slow")
    snake.goto(position)
    segments.append(snake)

def move_up():
    segments[0].setheading(90)
def move_down():
    segments[0].setheading(270)
def move_left():
    segments[0].setheading(180)
def move_right():
    segments[0].setheading(0)

screen.onkey(move_up,"Up")
screen.onkey(move_down,"Down")
screen.onkey(move_right,"Right")
screen.onkey(move_left,"Left")

screen.listen()

def move():
    for i in range(len(segments) - 1, 0, -1):
        new_x = segments[i - 1].xcor()
        new_y = segments[i - 1].ycor()
        segments[i].goto(new_x, new_y)

    segments[0].forward(20)
    # head_x = segments[0].xcor()
    # head_y = segments[0].ycor()
    #
    # segments[0].goto(head_x + 20,head_y)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    move()



screen.mainloop()

screen.exitonclick()

