from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(bg=BACKGROUND_COLOR)
window.title("Flashy")

random_card = {}

def next_card():
    # show a random word
    global random_card,flip_timer
    window.after_cancel(flip_timer)
    random_card = random.choice(record_data)
    canvas.itemconfig(title,text="Germany",fill="blue")
    canvas.itemconfig(word,text=random_card["Germany"],fill="black")
    canvas.itemconfig(canvas_image,image=front_image)
    flip_timer = window.after(ms=3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title,text="English",fill="black")
    canvas.itemconfig(word,text=random_card["English"],fill="white")
    canvas.itemconfig(canvas_image,image=back_image)


# read data
df = pandas.read_csv("data/language_data.csv")
record_data = df.to_dict(orient="records")



canvas = Canvas(window,width=800,height=526)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400,263,image= front_image)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
title =canvas.create_text(400,150,text="",fill="blue",font=("Arial", 20, "bold"))
word = canvas.create_text(400,263,text="",font=("Arial", 20, "bold"))

# flip the card
flip_timer = window.after(ms=3000,func=flip_card)

canvas.grid(row=0,column=1)


# buttons
wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=0,column=0)

right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image,highlightthickness=0,command=next_card)
known_button.grid(row=0,column=2)


next_card()
window.mainloop()

