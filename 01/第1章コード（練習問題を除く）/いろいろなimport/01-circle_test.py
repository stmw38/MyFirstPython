import tkinter
import math as mt

OX = 400
OY = 300
MAX_X = 800
MAX_Y = 600
SCALE_X = 100
SCALE_Y = 100

START = 0
END = 2*mt.pi
DELTA = 0.01

def draw_point(x, y, r=1, c="black"):
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=c, outline=c)

def make_axes(ox, oy, width, height):
    canvas.create_line(0, oy, width, oy)
    canvas.create_line(ox, 0, ox, height)

def plot(x, y):
    draw_point(SCALE_X * x + OX, OY - SCALE_Y * y)

def f1(x):
    return mt.cos(x)

def f2(x):
    return mt.sin(x)

tk = tkinter.Tk()
canvas = tkinter.Canvas(tk, width=800, height=600, bd=0)
canvas.pack()

make_axes(OX, OY, MAX_X, MAX_Y)

theta = START
while theta < END:
    plot(f1(theta), f2(theta))
    theta = theta + DELTA

tk.mainloop()
