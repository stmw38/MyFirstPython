from tkinter import *
from dataclasses import dataclass


@dataclass
class Car:
    w: int
    h: int
    a: int
    b: int
    wheel_color: str
    body_color: str


def draw_car_at(x, y, w, h, a, b, wheel_color, body_color):
    wtop_y = y + h / 2  # 縦からみて四角形の中心
    bottom_x = x + w  # 位置するx軸と横の長さ
    bottom_y = y + h  # 位置するy軸と縦の長さ

    canvas.create_rectangle(x, wtop_y, bottom_x, bottom_y, outline=body_color, fill=body_color)
    canvas.create_oval(a, 180, a + 30, 210, outline=wheel_color, fill=wheel_color)
    canvas.create_oval(b, 180, b + 30, 210, outline=wheel_color, fill=wheel_color)


def draw_car(car, x, y):
    w = car.w
    h = car.h
    a = car.a
    b = car.b
    wheel_color = car.wheel_color
    body_color = car.body_color
    draw_car_at(x, y, w, h, a, b, wheel_color, body_color)


tk = Tk()

canvas = Canvas(tk, width=500, height=400, bd=0, bg="whitesmoke")
canvas.pack()

cars = [
    Car(150, 200, 100, 30, "green", "white"),
    Car(100, 200, 170, 220, "blue", "gray"),
    Car(60, 200, 270, 300, "blue", "white"),
    Car(300, 200, 350, 450, "red", "orange"),
]

x = 0
y = 0
PAD = 10

for car in cars:
    draw_car(car, x, y)
    x += car.w + PAD

tk.mainloop()
