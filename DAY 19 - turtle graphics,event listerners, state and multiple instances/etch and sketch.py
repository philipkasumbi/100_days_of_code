from turtle import Turtle,Screen

# create a turtle named tom
tom = Turtle()
screen = Screen()


def move_forward():
    tom.forward(20)
def move_bk():
    tom.bk(20)
def clockwise():
    tom.right(360)
    tom.circle(50)
def counter_clockwise():
    tom.left(360)
    tom.circle(40)
def clear():
    tom.clear()
    tom.penup()
    tom.home()

screen.listen()
screen.onkey(fun=move_forward,key="w")
screen.onkey(fun=move_bk,key="s")
screen.onkey(fun=counter_clockwise,key="a")
screen.onkey(fun=clockwise,key="d")
screen.onkey(fun=clear,key="c")


screen.exitonclick()
