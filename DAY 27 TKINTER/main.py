# import tkinter
from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("First GUI Program")
window.minsize(height=300,width=500)
window.config(padx=50,pady=50)

# label
my_label = Label(text="I am a Label",font=("Arial",24,"bold"))

# changing the  label text
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0,row=0)
my_label.config(padx=50,pady=50)

# button
button = Button(text="Click Me",command=button_clicked)
button.grid(column=1,row=1)
button.config(padx=10,pady=10)

# Entry
input = Entry(width=10)
input.grid(column=2,row=2)







window.mainloop()