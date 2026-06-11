from tkinter import *
from quiz import  Questions,question_bank

THEME_COLOR = "#375362"
RIGHT_COLOR = "#90EE90"
WRONG_COLOR = "#FF7F7F"

window = Tk()
window.title("Quiz App")
window.config(bg=THEME_COLOR,pady=30,padx=30)

question = Questions(question_bank)

text_label = Label(window, text=f"score:{question.score}")
text_label.config(bg=THEME_COLOR, fg="white", font=("Helvetica", 20, "bold"))
text_label.grid(row=0, column=2, pady=30)


canvas = Canvas(width=400,height=300)
canvas.grid(row=1,column=1,padx=50)
question_text =canvas.create_text(200, 150, text="Now Goes the questions ", width=300, font=("Helvetica", 16, "bold"))


canvas.itemconfig(question_text,text=question.show_current())

def display_next_question():
    canvas.config(bg="white")
    question.next_question()
    canvas.itemconfig(question_text,text=question.show_current())

def correct_answer():
    user_answer = "True"
    if user_answer == question.check_answer_check():
        canvas.config(bg=RIGHT_COLOR)
        question.score += 1
        text_label.config(text=f"score:{question.score}")
    else:
        canvas.config(bg=WRONG_COLOR)

    window.after(1000,display_next_question)

def wrong_answer():
    user_answer = "False"
    if user_answer == question.check_answer_check():
        canvas.config(bg=RIGHT_COLOR)
        question.score += 1
        text_label.config(text=f"score:{question.score}")
    else:
        canvas.config(bg=WRONG_COLOR)

    window.after(1000,display_next_question)

right_image = PhotoImage(file="images/right.png")
right_image_button = Button(window, image=right_image,command=correct_answer)
right_image_button.grid(row=2,column=0,pady=30)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_image_button = Button(window,image=wrong_image,command=wrong_answer)
wrong_image_button.grid(row=2,column=2,pady=30)



window.mainloop()
