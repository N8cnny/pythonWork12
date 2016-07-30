from tkinter import *
global s
s = "Result:\n"


class MyError1(Exception):
    pass


def checkstr(x):
    if not x.isdigit():
        raise MyError1("Must be digits")
    else:
        return "True"
x = ["21", "3.4", "s123", "apple", "0"]
for i in x:

    try:
        s += i + ":" + checkstr(i) + "\n" # can raise the exception
    except MyError1 as ex:
        s += str(ex) + "\n"


class MyError2(Exception):
    pass


def checkeven(i):
    if int(i) % 2 == 0:
        return i
    else:
        raise MyError2("Not an even number.")
for i in range(1, 21):
    try:
        s += str(checkeven(i)) + "\n"
    except MyError2 as ex:
        s += str(i) + ": " + str(ex) + "\n"


class MyError(Exception):
    pass


def min(a, b):
    if a == b:
        raise MyError("Two equal values.")
    elif a > b:
        return a
    else:
        return b
try:
    s += str(min(2, 2)) + "\n"
except MyError as ex:
    s += str(ex) + "\n"

root = Tk()

root.title('Message Box')
Label(root, justify=LEFT, text=s).grid()

root.mainloop()
