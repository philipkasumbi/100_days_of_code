from turtle import Turtle,Screen

timmy_the_turtle = Turtle()

for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

# drawing dashed lines

tom = Turtle()

for _ in range(15):
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()

# draw the turtle in triangle to decagon shape 
terry = Turtle()

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        terry.forward(100)
        terry.right(angle)

for shapes_side_n in range(3,10):
    draw_shape(shapes_side_n)














screen = Screen()
screen.exitonclick()