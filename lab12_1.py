from tkinter import *

s = "results:\nExample 1:\n"
try:
    n = 5
    s += str(n/0) + "\n"
except Exception:
    s += "Nothing can be divided by zero. \n"

s += "Example 2:\n"
i = -5
while i < 5:
    try:
        s += str(7/i) + " "
    except Exception:
        s += "N/A "

    i = i + 1
s += "\n"

s += "Example 3:\n"
try:
    file = open("c:\windows\init1.ini", "r")
    s += file.name + "\n"
    s += file.mode + "\n"
except IOError as ex:
    s += str(ex) + "\n"

s += "Example 4:\n"
for i in range(-4, 4):
    try:
        s += str(7/i) + " "
    except Exception:
        s += "N/A "

# Message Box Code ######

root = Tk()

root.title('Message Box')
Label(root, justify=LEFT, text=s).grid()

root.mainloop()
