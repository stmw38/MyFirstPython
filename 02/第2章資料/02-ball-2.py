from tkinter import *
import time

DURATION = 0.001
STEPS = 1000
Y = 200
D = 10


def make_walls(ox, oy, width, height):
    canvas.create_rectangle(ox, oy, ox + width, oy + height)


tk = Tk()
canvas = Canvas(tk, width=800, height=600, bd=0)
canvas.pack()
tk.update()

x = 150
vx = 2

make_walls(100, 100, 600, 400)
id = canvas.create_rectangle(x, Y, x + D, Y + D, fill="darkblue", outline="black")

for s in range(STEPS):
    x = x + vx
    if x + D >= 700:
        vx = -vx
    elif x + D < 100:
        vx = -vx
    canvas.coords(id, x, Y, x + D, Y + D) # idが指定するオブジェクトの位置を変更する
    tk.update()
    time.sleep(DURATION)
