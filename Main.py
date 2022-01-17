# importing the tkinter module
from tkinter import *

# Creating an object from TK Class
root = Tk()
# Sets window size
root.geometry("430x500")
# an empty string to evaluate numeric expression
expression = ""


# Function to evaluate expression
def set_expression(num):
    global expression
    expression = expression + str(num)
    value.set(expression)


# Function to get the expression inputted from the user
def calculator():
    try:
        global expression
        answer = str(eval(expression))
        value.set(answer)
    except:
        value.set("Enter correct expression")
        expression = ""


# Function to clear the display area of the calculator
def clear():
    global expression
    expression = ""
    value.set(expression)


# Var to store the expression
value = StringVar(value="Enter expression")

# EW to create an input widget for the user
Entry(root, textvariable=value, font='Arial').grid(row=0, column=0, columnspan=4)

# Button widget to create buttons that calls set_expression function
B_add = Button(root, text="+", fg="white", bg="black", command=lambda:
set_expression("+"), height=4, width=8).grid(row=1, column=0)

B_sub = Button(root, text="-", fg="white", bg="black", command=lambda:
set_expression("-"), height=4, width=8).grid(row=2, column=0)

B_mul = Button(root, text="X", fg="white", bg="black", command=lambda:
set_expression("*"), height=4, width=8).grid(row=3, column=0)

B_div = Button(root, text="/", fg="white", bg="black", command=lambda:
set_expression("/"), height=4, width=8).grid(row=4, column=0)

B_1 = Button(root, text="1", fg="white", bg="black", command=lambda:
set_expression("1"), height=4, width=8).grid(row=1, column=1)

B_2 = Button(root, text="2", fg="white", bg="black", command=lambda:
set_expression("2"), height=4, width=8).grid(row=1, column=2)

B_3 = Button(root, text="3", fg="white", bg="black", command=lambda:
set_expression("3"), height=4, width=8).grid(row=1, column=3)

B_4 = Button(root, text="4", fg="white", bg="black", command=lambda:
set_expression("4"), height=4, width=8).grid(row=2, column=1)

B_5 = Button(root, text="5", fg="white", bg="black", command=lambda:
set_expression("5"), height=4, width=8).grid(row=2, column=2)

B_6 = Button(root, text="6", fg="white", bg="black", command=lambda:
set_expression("6"), height=4, width=8).grid(row=2, column=3)

B_7 = Button(root, text="7", fg="white", bg="black", command=lambda:
set_expression("7"), height=4, width=8).grid(row=3, column=1)

B_8 = Button(root, text="8", fg="white", bg="black", command=lambda:
set_expression("8"), height=4, width=8).grid(row=3, column=2)

B_9 = Button(root, text="9", fg="white", bg="black", command=lambda:
set_expression("9"), height=4, width=8).grid(row=3, column=3)

B_0 = Button(root, text="0", fg="white", bg="black", command=lambda:
set_expression("0"), height=4, width=8).grid(row=4, column=1)

B_dot = Button(root, text=".", fg="white", bg="black", command=lambda:
set_expression("."), height=4, width=8).grid(row=4, column=2)

# show the calculated value in the entry widget
Button(root, text="=", fg="white", bg="black", command=calculator, height=4,
       width=8).grid(row=4, column=3)

# Button that clears the entry widget
Button(root, text="Clear", fg="white", bg="black", command=clear, height=4,
       width=8).grid(row=5, column=0)

# Loop for everything to run on
root.mainloop()
