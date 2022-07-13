from tkinter import *
from dataclasses import dataclass


@dataclass
class Car:
    w: int
    h: int
    wheel_color_1: str
    wheel_color_2: str
    body_color: str


def draw_car_at(x, y, w, h, wheel_color_1, wheel_color_2, body_color):
    wtop_y = y + h / 2  # 縦からみて四角形の中心
    bottom_x = x + w  # 位置するx軸と横の長さ
    bottom_y = y + h  # 位置するy軸と縦の長さ

    canvas.create_rectangle(x, wtop_y, bottom_x, bottom_y, outline=body_color, fill=body_color)
    canvas.create_oval(150, 180, 180, 210, outline=wheel_color_1, fill=wheel_color_1)
    canvas.create_oval(30, 180, 60, 210, outline=wheel_color_2, fill=wheel_color_2)


def draw_car(car, x, y):
    w = car.w
    h = car.h
    wheel_color_1 = car.wheel_color_1
    wheel_color_2 = car.wheel_color_2
    body_color = car.body_color
    draw_car_at(x, y, w, h, wheel_color_1, wheel_color_2, body_color)

tk = Tk()

canvas = Canvas(tk, width=1000, height=800, bd=0)
canvas.pack()

car = Car(200, 200, "red", "red", "gray")
print(car)
draw_car(car, 0, 0)

tk.mainloop()
