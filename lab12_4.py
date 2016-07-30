from tkinter import *
import math
s = "result:\n"

x = -17
try:
    (math.sqrt(x))
except:
    pass
    s = str(math.sqrt(x*-1)) + "i\n"

try:
    math.pow(0, x)
except:
    pass
    s += str(math.pow(0, 1/(x*-1))) + "\n"

x = -451.726908
try:
    s += str(math.pow(x, 1/3)) + "\n"
except:
    pass
    s += str(math.pow(x*-1, 1/3)*-1) + "\n"

for i in range(-4, 4):
    try:
        s += str(5/i) + " "
    except:
        pass
        s += "NaN" + " "

s += "\n"

x = 71.915456
y = math.pow(math.sqrt(x), 1/3)
z = math.pow(y*y, 3)

if z != x:
    z = x

s += str(z) + "\n"

root = Tk()

root.title('Message Box')
Label(root, justify=LEFT, text=s).grid()

root.mainloop()
