
from tkinter import *

window = Tk()

window.geometry('350x200')

window.title("Welcome to @python.instructions")

lbl = Label(window, text="Hello @python.instructions",
        font=("Arial Bold", 10))

lbl.grid(column=0, row=0)

window.mainloop()


