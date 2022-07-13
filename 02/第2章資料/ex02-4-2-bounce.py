from tkinter import *
from dataclasses import dataclass
import time

DURATION = 0.001
# X0 = 150
# Y0 = 150
# D = 15
# VX0 = 2
# VY0 = 2

INFECTION_COL = "black"
RECOVERTIME = 500


@dataclass
class Ball:
    id: int
    x: int
    y: int
    d: int
    vx: int
    vy: int #
    c: str
    inf_t: int

@dataclass
class Border:
    left: int
    right: int
    top: int
    bottom: int

#
def make_ball(x, y, d=3, vx=2, vy=2, c=INFECTION_COL):
    id = canvas.create_rectangle(x, y, x + d, y + d, fill=c, outline=c)
    if c == INFECTION_COL:
        return Ball(id, x, y, d, vx, vy, c, RECOVERTIME)
    else:
        return Ball(id, x, y, d, vx, vy, c, 0)


def move_ball(ball):
    ball.x = ball.x + ball.vx
    ball.y = ball.y + ball.vy #


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
    make_ball(100, 150, 20, 2, 2, "orange"), #
    make_ball(200, 250, 25, -4, -4, "orange"), #
    make_ball(300, 350, 10, -2, -2, INFECTION_COL), #
    make_ball(400, 450, 5, 4, 4, "red"), #
]

while True:
    for ball in balls:
        move_ball(ball)

        if ball.x + ball.vx < border.left or ball.x + ball.d >= border.right:
            ball.vx = - ball.vx

        if ball.y + ball.vy < border.top or ball.y + ball.d >= border.bottom: #
            ball.vy = - ball.vy

        redraw_ball(ball)

    # 以下、当たり判定（読みやすさ重視？）
    for ball in balls:
        if ball.c == INFECTION_COL: #感染したボール
            for another in balls:
                if ball.id != another.id and another.c != INFECTION_COL:
                    dist_x = (ball.x + ball.d/2) - (another.x + another.d/2)
                    dist_y = (ball.y + ball.d/2) - (another.y + another.d/2)
                    if dist_x < 0:
                        dist_x = -dist_x
                    if dist_y < 0:
                        dist_y = -dist_y
                    if dist_x <= (ball.d + another.d)/2 and dist_y <= (ball.d + another.d)/2:
                        another.c = INFECTION_COL
                        another.inf_t = RECOVERTIME
                        canvas.itemconfigure(another.id, fill=another.c, outline=another.c)
                        redraw_ball(another)

    # 以下、回復判定
    for ball in balls:
        if ball.c == INFECTION_COL:
            ball.inf_t -= 1
        if ball.inf_t <= 0:
            ball.c = "green"
            canvas.itemconfigure(ball.id, fill=ball.c, outline=ball.c)
            redraw_ball(ball)

    tk.update()
    time.sleep(DURATION)

    # 以下、終了判定
    count = 0
    for ball in balls:
        if ball.c == INFECTION_COL:
            count += 1
    if count == 0:
        break
