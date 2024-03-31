from tkinter import *

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("First Program")
window.minsize(width=500, height=300)
my_label = Label(text="im label")
my_label.grid(column=0, row=0)


button = Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)

#entry
input = Entry(width=10)
input.grid(column=2, row=2)

window.mainloop()
