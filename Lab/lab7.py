import tkinter as tk
from tkinter import ttk

# create the root window
root = tk.Tk()

# modify the window
root.title("Simple Calculator")
root.geometry("600x500")

# create a frame in the window to hold other widgets
Calci = ttk.Frame(root, padding="50 50 50 50")
Calci.pack()

# create a label for no1 in the frame
no1Label = ttk.Label(Calci, text="Enter first no: ")
no1Label.grid(column=0, row=0)

# create textbox for no1 in the frame
no1 = tk.StringVar()
ttk.Entry(Calci, width=25, textvariable=no1).grid(column=1, row=0)

# create a label for no2 in the frame
no2Label = ttk.Label(Calci, text="Enter second no: ")
no2Label.grid(column=0, row=1)

# create textbox for no2 in the frame
no2 = tk.StringVar()
ttk.Entry(Calci, width=25, textvariable=no2).grid(column=1, row=1)

# add callback function


def add():
    num1 = float(no1.get())
    num2 = float(no2.get())
    res.set(num1+num2)

# sub callback function


def sub():
    num1 = float(no1.get())
    num2 = float(no2.get())
    res.set(num1-num2)

# mul callback function


def mul():
    num1 = float(no1.get())
    num2 = float(no2.get())
    res.set(num1*num2)

# div callback function


def div():
    num1 = float(no1.get())
    num2 = float(no2.get())
    if num2 == 0:
        res.set("Divide by zero error")
    else:
        res.set(num1/num2)


# Buttons for basic arithmetic operations
ttk.Button(Calci, text="Add", command=add).grid(column=0, row=2)
ttk.Button(Calci, text="Sub", command=sub).grid(column=1, row=2)
ttk.Button(Calci, text="Mul", command=mul).grid(column=0, row=3)
ttk.Button(Calci, text="Div", command=div).grid(column=1, row=3)

# Readonly textbox for result
res = tk.StringVar()
ttk.Entry(Calci, width=25, textvariable=res,
          state="readonly").grid(column=1, row=4)

# Configuring the widgets
for child in Calci.winfo_children():
    child.grid_configure(padx=5, pady=5)

# kick off the window's event loop
root.mainloop()
