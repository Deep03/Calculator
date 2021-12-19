# importing the tkinter module
from tkinter import *

# initializing the tkinter, creating an object
root = Tk()
# setting the width and height of the gui window
root.geometry("430x500")
# declaring an empty string variable for expression to be added on
expression = ""


# Function to evaluating expression
def set_expression(num):
    global expression
    expression = expression + str(num)
    value.set(expression)

# defining a function to calculate the expression entered by the user
def calculator():
    try:
        global expression
        answer = str(eval(expression))
        value.set(answer)
    except:
        value.set("Enter correct expression")
        expression = ""


# function to clear everything in expression
def clear():
    global expression
    expression = ""
    value.set(expression)


# Variable to store data entered by user
value = StringVar(value="Enter expression")

# Entry widget to accept data from user and store it in value
Entry(root, textvariable=value, font='Arial').grid(row=0,
                                                   column=0, columnspan=4)

B_add = Button(root, text="+", fg="white", bg="black", command=lambda:
set_expression("+"), height=4, width=8).grid(row=1, column=0)

B_subtract = Button(root, text="-", fg="white", bg="black", command=lambda:
set_expression("-"), height=4, width=8).grid(row=2, column=0)

B_mul = Button(root, text="X", fg="white", bg="black", command=lambda:
set_expression("*"), height=4, width=8).grid(row=3, column=0)

B_divide = Button(root, text="/", fg="white", bg="black", command=lambda:
set_expression("/"), height=4, width=8).grid(row=4, column=0)

B_one = Button(root, text="1", fg="white", bg="black", command=lambda:
set_expression("1"), height=4, width=8).grid(row=1, column=1)

B_two = Button(root, text="2", fg="white", bg="black", command=lambda:
set_expression("2"), height=4, width=8).grid(row=1, column=2)

B_three = Button(root, text="3", fg="white", bg="black", command=lambda:
set_expression("3"), height=4, width=8).grid(row=1, column=3)

B_four = Button(root, text="4", fg="white", bg="black", command=lambda:
set_expression("4"), height=4, width=8).grid(row=2, column=1)

B_five = Button(root, text="5", fg="white", bg="black", command=lambda:
set_expression("5"), height=4, width=8).grid(row=2, column=2)

B_six = Button(root, text="6", fg="white", bg="black", command=lambda:
set_expression("6"), height=4, width=8).grid(row=2, column=3)

B_seven = Button(root, text="7", fg="white", bg="black", command=lambda:
set_expression("7"), height=4, width=8).grid(row=3, column=1)

B_eight = Button(root, text="8", fg="white", bg="black", command=lambda:
set_expression("8"), height=4, width=8).grid(row=3, column=2)

B_nine = Button(root, text="9", fg="white", bg="black", command=lambda:
set_expression("9"), height=4, width=8).grid(row=3, column=3)

B_zero = Button(root, text="0", fg="white", bg="black", command=lambda:
set_expression("0"), height=4, width=8).grid(row=4, column=1)

B_decimal = Button(root, text=".", fg="white", bg="black", command=lambda:
set_expression("."), height=4, width=8).grid(row=4, column=2)

# show the calculated value in the entry widget
Button(root, text="=", fg="white", bg="black", command=calculator, height=4,
       width=8).grid(row=4, column=3)

# "Clear" button to call the clear function which will clear the
# entry widget so that the user can start calculating again
Button(root, text="Clear", fg="white", bg="black", command=clear, height=4,
       width=20).grid(row=5, column=1)

# .mainloop() is used when the code is ready to run
root.mainloop()
