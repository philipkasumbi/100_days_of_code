from tkinter import *

window = Tk()
window.title("Miles to Km converter")
window.minsize(width=400,height=400)
window.config(padx=40,pady=40)

# inputs
input_miles = Entry(width=10,font=("Arial", 16))
input_miles.grid(column=0,row=0,padx=10,pady=10)

input_km = Entry(width=10,font=("Arial", 16))
input_km.grid(column=1,row=1)

# labels
miles = Label(text="Miles",font=("Arial",20,"bold"))
miles.grid(row=0,column=1)

is_equal_to = Label(text="Is equal to",font=("Serif",20,"bold"))
is_equal_to.grid(row=1,column=0)

km = Label(text="Km",font=("Arial",20,"bold"))
km.grid(row=1,column=2)

# conversion function
def calculate():
    value = input_miles.get()

    if value != "":
        mile = float(value)
        result = round(mile * 1.60934)
        input_km.insert(0,result)

# button
calculate_button = Button(text="Calculate",font=("Arial",15,"bold"),command= calculate)
calculate_button.grid(row=2,column=1)

window.mainloop()