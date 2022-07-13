from tkinter import *
from dataclasses import dataclass
import time

DURATION = 0.001
# X0 = 150
# Y0 = 150
# D = 15
# VX0 = 2


@dataclass
class Ball:
    id: int
    x: int
    y: int
    d: int
    vx: int
    c: str


@dataclass
class Border:
    left: int
    right: int
    top: int
    bottom: int


def make_ball(x, y, d=3, vx=2, c="black"):
    id = canvas.create_rectangle(x, y, x + d, y + d, fill=c, outline=c)
    return Ball(id, x, y, d, vx, c)


def move_ball(ball):
    ball.x = ball.x + ball.vx


def make_walls(ox, oy, width, height):
    canvas.create_rectangle(ox, oy, ox + width, oy + height)


def redraw_ball(ball):
    d = ball.d
    canvas.coords(ball.id, ball.x, ball.y, ball.x + d, ball.y + d)


tk = Tk()
canvas = Canvas(tk, width=800, height=600, bd=0)
canvas.pack()
tk.update()

border = Border(100, 700, 100, 500)

make_walls(border.left, border.top, border.right - border.left, border.bottom - border.top)
balls = [
    make_ball(100, 150, 20, 2, "darkblue"),
    make_ball(200, 250, 25, -4, "orange"),
    make_ball(300, 350, 10, -2, "orange"),
    make_ball(400, 450, 5, 4, "darkgreen"),
]

while True:
    for ball in balls:
        move_ball(ball)

        if ball.x + ball.vx < border.left or ball.x + ball.d >= border.right:
            ball.vx = - ball.vx

        redraw_ball(ball)

    tk.update()
    time.sleep(DURATION)
