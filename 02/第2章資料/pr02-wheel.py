from tkinter import *
from dataclasses import dataclass
import time

DURATION = 0.001
X = 0
Y = 100
D = 10


@dataclass
class Ball:
    id1: int
    id2: int
    x: int
    y: int
    d: int
    c: str


def make_ball(x, y, d=3, c="black"):
    id1 = canvas.create_oval(150, 180, 180, 210, fill=c, outline=c)
    id2 = canvas.create_oval(30, 180, 60, 210, fill=c, outline=c)

    return Ball(id1, id2, x, y, d, c)


def redraw_ball(ball):
    d = ball.d
    canvas.coords(ball.id1, 150, 180, 180, 210)
    canvas.coords(ball.id2, 30, 180, 60, 210)


tk = Tk()
canvas = Canvas(tk, width=800, height=600, bd=0)
canvas.pack()
tk.update()

ball = make_ball(X, Y, D, "darkblue")

for p in range(0, 600, 2):
    ball.x = p
    redraw_ball(ball)
    tk.update()
    time.sleep(DURATION)
