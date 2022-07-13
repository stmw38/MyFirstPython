from tkinter import *
import math

OX = 400
OY = 300
MAX_X = 800
MAX_Y = 600
SCALE_X = 80
SCALE_Y = 80

START = -5.0
END = 5.0
DELTA = 0.01

def draw_point(x, y, r = 1, c = "black"):
    canvas.create_oval(x - r, y - r, x + r, y + r, fill = c, outline = c)

def make_axes(ox, oy, width, height):
    canvas.create_line(0, oy, width, oy)
    canvas.create_line(ox, 0, ox, height)

def plot(x, y):
    draw_point(SCALE_X * x + OX, OY - SCALE_Y * y)

def f(x):
    return x * x

tk = Tk()
canvas = Canvas(tk, width=MAX_X, height = MAX_Y)
canvas.pack()

make_axes(OX, OY, MAX_X, MAX_Y)

x = START
while x < END:
    plot(x, f(x))
    x = x + DELTA

tk.mainloop()
