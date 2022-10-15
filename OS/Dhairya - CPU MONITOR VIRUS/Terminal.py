from tkinter.filedialog import *
import tkinter as tk
from tkinter import *
import subprocess
from subprocess import check_output
import os

def clear():
    entry.delete(1.0,END)

def run():
    text = str(entry.get(1.0, END))
    arr = text.split()
    command = subprocess.run(arr)
    out = check_output(arr)
    entry.delete(1.0,END)
    entry.insert(INSERT, out)
    pass

canvas = tk.Tk()
canvas.geometry("1280x720")
canvas.configure(background='black')
canvas.title("Terminal")
canvas.config(background="black")
top = Frame(canvas)
top.pack(padx = 10, pady = 5, anchor = 'nw')

b1 = Button(canvas, text="Run", bg = "Red", command = run)
b1.pack(in_ = top, side=LEFT)
b2 = Button(canvas, text="Clear", bg = "Blue", command = clear)
b2.pack(in_=top, side=RIGHT)

entry = Text(canvas, wrap = WORD, bg = "black", font = ("poppins", 15), fg='white')
entry.pack(padx = 10, pady = 5, expand = TRUE, fill = BOTH)

canvas.mainloop()