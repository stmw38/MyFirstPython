from tkinter import *
from dataclasses import dataclass
import time

DURATION = 0.001
X = 0
Y = 100
D = 10


@dataclass
class Body:
    id1: int
    x: int
    y: int
    d: int
    c: str


def make_body(x, y, d=3, c="black"):
    id1 = canvas.create_rectangle(x, y, x + d * 20, y + d * 10, fill=c, outline=c)

    return Body(id1, x, y, d, c)


def redraw_body(body):
    d = body.d
    canvas.coords(body.id1, body.x, body.y, body.x + d * 20, body.y + d * 10)


tk = Tk()
canvas = Canvas(tk, width=800, height=600, bd=0)
canvas.pack()
tk.update()

body = make_body(X, Y, D, "darkblue")

for p in range(0, 600, 2):
    body.x = p
    redraw_body(body)
    tk.update()
    time.sleep(DURATION)
