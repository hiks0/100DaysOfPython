from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random as rd
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pass():
    passinput.delete(0, END)

    pass_letters = rd.randint(8, 10)
    pass_numbers = rd.randint(2, 4)
    pass_characters = rd.randint(2, 4)

    password_list = []

    for char in range(0, pass_letters):
        password_list.append(rd.choice(letters))

    for char in range(0, pass_numbers):
        password_list.append(rd.choice(numbers))

    for char in range(0, pass_characters):
        password_list.append(rd.choice(symbols))

    rd.shuffle(password_list)

    password = "".join(password_list)
    passinput.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = webinput.get()
    email = mailinput.get()
    password = passinput.get()
    new_data = {
        webinput.get(): {
            "email": mailinput.get(),
            "password": passinput.get()
        }
    }
    if webinput.get() == 0 or passinput.get() == 0 or mailinput.get() == 0:
        messagebox.showinfo(title="Error", message="Some fields are left empty")
    else:
        is_ok = messagebox.askokcancel(title=webinput.get(),
                                       message=f"Email: {mailinput.get()}\n Password: {passinput.get()}\n Proceed to save?")
        if is_ok:
            with open("pass_data.csv", "a") as data_file:
                data_file.write(f"{webinput.get()}, {mailinput.get()}, {passinput.get()}\n")
            with open("password_data.txt", "a") as data_file:
                data_file.write(f"{webinput.get()} | {mailinput.get()} | {passinput.get()}\n")
            try:
                with open("data.json", "r") as data_file:
                #Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
            #Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                #Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                webinput.delete(0, END)
                passinput.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.config(pady=50, padx=50)
screen.title("Password Manager")

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

l1 = Label(text="Website:")
l1.grid(row=1, column=0)

l2 = Label(text="Email/username:")
l2.grid(row=2, column=0)

l3 = Label(text="Password:")
l3.grid(column=0, row=3)

webinput = Entry(width=35)
webinput.grid(row=1, column=1, columnspan=1)
webinput.focus()

mailinput = Entry(width=35)
mailinput.grid(row=2, column=1, columnspan=2)
mailinput.insert(0, "pranaymathur4@gmail.com")

passinput = Entry(width=18)
passinput.grid(column=1, row=3)

generate = Button(text="Generate Password", command=generate_pass)
generate.grid(column=2, row=3)

addbutton = Button(text="Add", width=36, command=save)
addbutton.grid(column=1, row=4, columnspan=2)



screen.mainloop()
