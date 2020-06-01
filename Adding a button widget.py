

from tkinter import *

window = Tk()

window.title("Welcome to @python.instructions")

window.geometry('350x200')

lbl = Label(window, text="@python.instructions")

lbl.grid(column=0, row=0)

def clicked():

    lbl.configure(text="Button was clicked !!")

btn = Button(window, text="Click Me", bg="orange", fg="red")

btn.grid(column=1, row=0)

window.mainloop()