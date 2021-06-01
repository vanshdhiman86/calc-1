import tkinter
from tkinter import *
from tkinter import messagebox
from functools import partial
win = Tk()
win.title("Calc")
win.configure(bg='pink')
win.geometry("300x100")
def sum(label, x1, x2):
    n1 = (x1.get())
    n2 = (x2.get())
    sum = float(n1) + float(n2)
    label.config(text = "sum is : %f" %sum)
    return
def sub(label, x1, x2):
    n1 = (x1.get())
    n2 = (x2.get())
    sub = float(n1) - float(n2)
    label.config(text = "subtraction is : %f" %sub)
    return
def div(label, x1, x2):
    try:
        n1 = (x1.get())
        n2 = (x2.get())
        div = float(n1) / float(n2)
        label.config(text = "division is : %f" %div)
    except:
        label.config(text = "division is : ∞")
    return
def mul(label, x1, x2):
    n1 = (x1.get())
    n2 = (x2.get())
    mul = int(n1) * int(n2)
    label.config(text = "product is : %f" %mul)
    return

l1 = Label(win,text = "first no", background = "pink")
l1.grid(row = 1, column = 0)
l2 = Label(win,text = "second no", background = "pink")
l2.grid(row = 2, column = 0)
label = Label(win, background = "pink")
label.place(x = 120, y = 50)

x1 = StringVar()
x2 = StringVar()

e1 = Entry(win,textvariable = x1)
e1.grid(row = 1, column = 2)
e2 = Entry(win,textvariable = x2)
e2.grid(row = 2, column = 2)
sum = partial(sum,label,x1,x2)
sub = partial(sub,label,x1,x2)
div = partial(div,label,x1,x2)
mul = partial(mul,label,x1,x2)
button = Button(win, text = "+", command = sum)
button.place(x = 0, y = 50)
button = Button(win, text = "-", command = sub)
button.place(x = 30, y = 50)
button = Button(win, text = "/", command = div)
button.place(x = 60, y = 50)
button = Button(win, text = "*", command = mul)
button.place(x = 90, y = 50)

win.mainloop()
