from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(bg=BACKGROUND_COLOR,height=700)
window.title("Flashy")

# read data
df = pandas.read_csv("data/language_data.csv")
record_data = df.to_dict(orient="records")

# show a random word
random_card = random.choice(record_data)
print(random_card["Germany"])

canvas = Canvas(window,width=800,height=526)

front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image= front_image)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.create_text(400,150,text="Germany",fill="blue",font=("Arial", 20, "bold"))
canvas.create_text(400,263,text=random_card["Germany"],font=("Arial", 20, "bold"))
canvas.grid(row=0,column=1)


# buttons
wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image,highlightthickness=0)
unknown_button.grid(row=0,column=0)

right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image,highlightthickness=0)
known_button.grid(row=0,column=2)



window.mainloop()

