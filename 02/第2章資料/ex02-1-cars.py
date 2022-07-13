from tkinter import *
from dataclasses import dataclass
import time

DURATION = 0.001


@dataclass
class Car:
    id1: int
    id2: int
    id3: int
    x: int
    y: int
    d: int
    vx: int
    bc: str
    wc: str

@dataclass
class Border:
    left: int
    right: int
    top: int
    bottom: int


def make_car(x, y, d, vx, bc="black", wc="black"):
    id1 = canvas.create_rectangle(x, y, x + d, y + d, fill=bc, outline=bc)
    id2 = canvas.create_oval(0, 0, 0, 0, outline=wc, fill=wc)
    id3 = canvas.create_oval(0, 0, 0, 0, outline=wc, fill=wc)

    return Car(id1, id2, id3, x, y, d, vx, bc, wc)


def move_car(car):
    car.x = car.x + car.vx


def make_walls(ox, oy, width, height):
    canvas.create_rectangle(ox, oy, ox + width, oy + height)


def redraw_car(car):
    d = car.d
    canvas.coords(car.id1, car.x, car.y, car.x + d * 20, car.y + d * 10)
    canvas.coords(car.id2, car.x + 130, car.y + 80, car.x + d + 160, car.y + d + 110)
    canvas.coords(car.id3, car.x + 30, car.y + 80, car.x + d + 60, car.y + d + 110)


tk = Tk()
canvas = Canvas(tk, width=800, height=600, bd=0)
canvas.pack()
tk.update()

border = Border(100, 700, 100, 500)

make_walls(border.left, border.top, border.right - border.left, border.bottom - border.top)
cars = [
    make_car(100, 120, 10, 3, "blue", "red"),
    make_car(100, 320, 10, 10, "yellow", "black"),
]

while True:
    for car in cars:
        move_car(car)

        if car.x + car.vx < border.left or car.x + car.d >= border.right:
            car.vx = - car.vx

        redraw_car(car)

    tk.update()
    time.sleep(DURATION)
