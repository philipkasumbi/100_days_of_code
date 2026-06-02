from  tkinter import  *
from tkinter import  messagebox
from random import choice,randint,shuffle
import pyperclip
import json

# -------------------GENERATE PASSWORD-----------------
def generate_strong_password():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
               "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-"]

    password_letter = [choice(letters) for _ in range(randint(5,7))]
    password_symbol = [choice(symbols) for _ in range(randint(1, 2))]
    password_number = [choice(numbers) for _ in range(randint(2,3))]

    password_list = password_letter + password_symbol + password_number
    shuffle(password_list)

    password = ''.join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0,password)


# ------------------SAVE PASSWORD---------------
# get text
def add_data():
    website_value = website_entry.get()
    username_value = username_entry.get()
    password_value = password_entry.get()
    new_data = {
        website_value:{
            "email":username_value,
            "password":password_value
        }

    }

    if len(website_value) == 0 or len(username_value) == 0 or len(password_value) == 0:
        messagebox.showinfo(title="Oops",message="Please don't leave any field empty")
    else:
        # is_okay = messagebox.askokcancel(title=website_value,message=f"These are the details you've entered:\nEmail: {username_value}"
        #                                                    f"\nPassword: {password_value}\nIs it okay to save?")
        # if is_okay:
        try:
            with open("data.json","r") as file:
                # reading old data
                data = json.load(file)
                # updating new data with old data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json","w") as file:
                # saving updated new data
                json.dump(new_data,file,indent=4)
        else:
            with open("data.json","r") as file:
                # reading old data
                data = json.load(file)
                # updating new data with old data
                data.update(new_data)
            with open("data.json","w") as file:
                # saving updated new data
                json.dump(data,file,indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

# -------------------------------SEARCH WEBSITE---------------------

def find_password():
    website_value = website_entry.get()
    with open("data.json","r") as file:
        data = json.load(file)

        if website_value in data:
            messagebox.showinfo(title=website_value,message=f"The email is: {data[website_value]["email"]} and the password is: {data[website_value]["password"]}")

        else:
            messagebox.showinfo(title="Oops",message="The website  not Found")


# ----------------------UI SETUP----------------
root = Tk()
root.title('Password Manager')
root.config(pady=50,padx=50)


# canvas
window = Canvas(height=300,width=300,highlightthickness=0)
my_image = PhotoImage(file="my_pass.png")
window.create_image(165,145,image= my_image)
window.grid(row=0,column=1)

# labels
website = Label(text="Website",font=("Arial",17,"bold"))
website.grid(row=1,column=0)

email = Label(text="Email/Username",font=("Arial",17,"bold"))
email.grid(row=2,column=0)

password = Label(text="Password",font=("Arial",17,"bold"))
password.grid(row=3,column=0)

# entries
website_entry = Entry(width=15,font=("Times New Roman",20))
website_entry.grid(row=1,column=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=30,font=("Times New Roman",20))
username_entry.grid(row=2,column=1, columnspan=2)
username_entry.insert(0,"philip@gmail.com")

password_entry = Entry(width=16,font=("Times New Roman",20))
password_entry.grid(row=3,column=1)

# buttons
generate_password = Button(text="Generate_password",command=generate_strong_password)
generate_password.grid(row=3,column=2)

search = Button(text="Search",width=10,font=("Times New Roman",14),command=find_password)
search.grid(row=1,column=2)

add = Button(text="Add",width=31,command=add_data)
add.grid(row=4,column=1,columnspan=2)


root.mainloop()