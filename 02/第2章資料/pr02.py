from tkinter import *
from dataclasses import dataclass
import time

DURATION = 0.001
X = 0
Y = 100
D = 10


@dataclass
class Car:
    id0: int
    id1: int
    id2: int
    id3: int
    x: int
    y: int
    l: int
    wr: int
    vx: int
    bcolor: str


def make_car(x, y, l, h, wr, vx, bcolor):
    id0 = canvas.create_rectangle(0, 0, 0, 0, fill=bcolor, outline=bcolor)
    id1 = canvas.create_oval(0, 0, 0, 0, fill="black", outline="black")
    id2 = canvas.create_oval(0, 0, 0, 0, fill="black", outline="black")
    ids = [id0, id1, id2]

    return Car(ids, x, y, l, h, wr, vx, bcolor)

def redraw_car(car):
    canvas.coords(car.ids, car.x, car.y, car.l, car.h, car.wr, car.vx)

tk = Tk()
canvas = Canvas(tk, width=800, height=600, bd=0)
canvas.pack()
tk.update()

car = make_car(X, Y, L, H, WR, VX, "blue")

for p in range(0, 600, 2):
    car.x = p
    redraw_car(car)
    tk.update()
    time.sleep(DURATION)
