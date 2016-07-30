from tkinter import *
import InputBox
s = "result:\nExample 1: "


InputBox.ShowDialog("Enter an integer: ")
x = int(InputBox.GetInput())
try:
    s += str(x / y) + "\n"
except NameError as ex:
    y = x * 2
    s += str(x / y) + "\n"
finally:
    s += "x is " + str(x) + ". y is " + str(y) + ".\n"


s += "Example 2: "
a = [0 for x in range(4)]
for i in range(5):
    try:
        a[i] = i
        msg = str(a[i])
    except IndexError:
        break
    else:
        s += msg + " "
s += "\n"


s += "Example 3: "
InputBox.ShowDialog("How old are you? ")
n = InputBox.GetInput()
while True:
    try:
        n = int(n)
    except ValueError:
        InputBox.ShowDialog("Age must be an integer, try again!")
        n = InputBox.GetInput()
    else:
        s += "You finally entered an integral value of age!\n"
        break


s += "Example 4: "
x = ["apple", "orange", "banana", "cherry", "tangerine"]
try:
    s += x[6] + "\n"
except IndexError as ex:
    s += "The list has only " + str(len(x)) + " elements.\n"


root = Tk()

root.title('Message Box')
Label(root, justify=LEFT, text=s).grid()

root.mainloop()

