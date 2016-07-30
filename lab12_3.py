from tkinter import *
import InputBox
s = "result:\nExample 1: "

try:
    s += str(10 * (1/0)) + "\n"
except ZeroDivisionError as ex:
    s += "Zero Division.\n"

s += "Example 2: "
while True:
    try:
        InputBox.ShowDialog("Enter a float-point number: ")
        n = float(InputBox.GetInput())
        s += str(n) + " is a floating-point number.\n"
        break
    except ValueError as ex:
        s += str(ex)

s += "Example 3: "
x = "cis247"
try:
    s += x[6] + "\n"
except IndexError as ex:
    s += str(ex) + ": s only has " + str(len(x)) + " elements.\n"

s += "Example 4: "
x = 5
try:
    z = x / y
except NameError:
    s += "y is undefined.\n"

s += "Example 5: "
InputBox.ShowDialog("Enter a number: ")
x = InputBox.GetInput()
try:
    x = x / 2
except TypeError as ex:
    x = float(x) / 2
finally:
    s += str(x) + "\n"

s += "Example 6: "
try:
    s += eval('5 times 4')
except SyntaxError as ex:
    s += str(ex) + "\n"

root = Tk()

root.title('Message Box')
Label(root, justify=LEFT, text=s).grid()

root.mainloop()
