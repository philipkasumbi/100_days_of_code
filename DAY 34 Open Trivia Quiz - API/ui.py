from tkinter import *
from quiz import  Questions,question_bank

THEME_COLOR = "#375362"

window = Tk()
window.title("Quiz App")
window.config(bg=THEME_COLOR,pady=30,padx=30)

label = Label(window,text= f"score:0")
label.config(bg=THEME_COLOR,fg="white",font=("Helvetica",20,"bold"))
label.grid(row=0,column=2,pady=30)


canvas = Canvas(width=400,height=300)
canvas.grid(row=1,column=1,padx=50)
question_text =canvas.create_text(200, 150, text="Now Goes the questions ", width=300, font=("Helvetica", 16, "bold"))

question = Questions(question_bank)
canvas.itemconfig(question_text,text=question.show_current())

right_image = PhotoImage(file="images/right.png")
right_image_button = Button(window, image=right_image)
right_image_button.grid(row=2,column=0,pady=30)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_image_button = Button(window,image=wrong_image)
wrong_image_button.grid(row=2,column=2,pady=30)



window.mainloop()
