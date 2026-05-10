from turtle import Turtle,Screen

# create a turtle named tom
tom = Turtle()
screen = Screen()

def move_forward():
    tom.forward(20)

screen.listen()
screen.onkey(fun=move_forward,key="space")


screen.exitonclick()
