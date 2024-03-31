from tkinter import *

screen = Tk()
screen.config(padx=20, pady=20)
screen.title("Mile to Km Converter")


def cal():
    m = float(input.get())
    k = m * 1.609344
    l2.config(text=k)


l1 = Label(text="is equal to")
l1.grid(column=0, row=1)

l2 = Label(text="0")
l2.grid(column=1, row=1)

l3 = Label(text="Miles")
l3.grid(column=2, row=0)

l4 = Label(text="Km")
l4.grid(column=2, row=1)

button = Button(text="Calculate", command=cal)
button.grid(column=1, row=2)

input = Entry(width=20)
input.grid(column=1, row=0)

screen.mainloop()
