import time
from turtle import Turtle,Screen
import pandas

writer = Turtle()
writer.hideturtle()
screen = Screen()
screen.title("U.S. States Game")
screen.setup(width=800, height=600)

screen.bgpic("blank_image.gif")

data = pandas.read_csv("50_states.csv")

guessed_state = []
score = 0

game_still_on = True

while game_still_on:
    answer_state = (screen.textinput(title=f"score: {score}/50", prompt="What's another state name")).title()
    if answer_state in data["state"].values and answer_state not in guessed_state:
        states_data_x = int(data[data["state"] == answer_state]["x"].item())
        states_data_y = int(data[data["state"] == answer_state]["y"].item())

        writer.hideturtle()
        writer.penup()
        writer.goto(states_data_x,states_data_y)
        writer.write(answer_state)
        score += 1
        guessed_state.append(answer_state)

        if score == 50:
            game_still_on = False



screen.mainloop()





