import tkinter as tk

root = tk.Tk()
root.title("Calculator")

expression = ""


# Create functions
def add(value):
    global expression
    expression += value
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, expression)


def clear():
    global expression
    expression = ""
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, expression)


def calculate():
    global expression
    try:
        expression = str(eval(expression))
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, expression)
    except:
        clear()
        text_result.insert(1.0, 'Error')


# Create GUI
text_result = tk.Text(root, height=2, width=39)
text_result.grid(columnspan=5)


button_1 = tk.Button(root, text="1", command=lambda: add("1"), width=10, height=2)
button_1.grid(row=2, column=1)

button_2 = tk.Button(root, text="2", command=lambda: add("2"), width=10, height=2)
button_2.grid(row=2, column=2)

button_3 = tk.Button(root, text="3", command=lambda: add("3"), width=10, height=2)
button_3.grid(row=2, column=3)

button_4 = tk.Button(root, text="4", command=lambda: add("4"), width=10, height=2)
button_4.grid(row=3, column=1)

button_5 = tk.Button(root, text="5", command=lambda: add("5"), width=10, height=2)
button_5.grid(row=3, column=2)

button_6 = tk.Button(root, text="6", command=lambda: add("6"), width=10, height=2)
button_6.grid(row=3, column=3)

button_7 = tk.Button(root, text="7", command=lambda: add("7"), width=10, height=2)
button_7.grid(row=4, column=1)

button_8 = tk.Button(root, text="8", command=lambda: add("8"), width=10, height=2)
button_8.grid(row=4, column=2)

button_9 = tk.Button(root, text="9", command=lambda: add("9"), width=10, height=2)
button_9.grid(row=4, column=3)

button_0 = tk.Button(root, text="0", command=lambda: add("0"), width=10, height=2)
button_0.grid(row=5, column=2)

button_add = tk.Button(root, text="+", command=lambda: add("+"), width=10, height=2)
button_add.grid(row=2, column=4)

button_divide = tk.Button(root, text="/", command=lambda: add("/"), width=10, height=2)
button_divide.grid(row=5, column=4)

button_multiply = tk.Button(root, text="*", command=lambda: add("*"), width=10, height=2)
button_multiply.grid(row=4, column=4)

button_subtract = tk.Button(root, text="-", command=lambda: add("-"), width=10, height=2)
button_subtract.grid(row=3, column=4)

button_open = tk.Button(root, text="(", command=lambda: add("("), width=10, height=2)
button_open.grid(row=5, column=1)

button_close = tk.Button(root, text=")", command=lambda: add(")"), width=10, height=2)
button_close.grid(row=5, column=3)

button_clear = tk.Button(root, text="C", command=lambda: clear(), width=21, height=2)
button_clear.grid(row=6, column=1, columnspan=2)

button_equals = tk.Button(root, text="=", width=21, command=lambda: calculate(), height=2)
button_equals.grid(row=6, column=3, columnspan=2)

root.geometry('322x250')

root.mainloop()