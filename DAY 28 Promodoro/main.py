from tkinter import *
import  math
# --------------------------------CONSTANTS-------------------------
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✅"
reps = 0
time = None

# --------------------------------TIMER RESET-------------------------
def reset_timer():
    window.after_cancel(time)
    canvas.itemconfig(timer_text,text="00:00")
    timer.config(text="Timer")
    checkmark.config(text="")

# --------------------------------TIMER MECHANISM-------------------------
def start_timer():
    global  reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="WORK", fg=GREEN)

# --------------------------------COUNTDOWN MECHANISM-------------------------
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count >0:
        global time
        time = window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark = " "
        working_sessions = math.floor(reps/2)

        for _ in range(working_sessions):
            mark += CHECKMARK

        checkmark.config(text=mark)
# --------------------------------UI SETUP-------------------------
window =Tk()
window.title("POMODORO TIMER")
window.config(padx=100,pady=50,bg=YELLOW)


# labels
timer = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,35,"bold"))
timer.grid(row=0,column=1)

# buttons
start = Button(text="Start",font=(FONT_NAME,27,"bold"),command=start_timer)
start.grid(row=2,column=0)

reset = Button(text="Reset",font=(FONT_NAME,27,"bold"),command=reset_timer)
reset.grid(row=2,column=2)

# checkmark
checkmark = Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,35,"bold"))
checkmark.grid(row=3,column=1)

canvas = Canvas(width=250,height=250,bg = YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(125,125,image=tomato_img)
timer_text = canvas.create_text(125,145,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)



window.mainloop()