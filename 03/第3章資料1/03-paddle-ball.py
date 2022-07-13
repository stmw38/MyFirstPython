from tkinter import *
from dataclasses import dataclass
import time
import random

DURATION = 0.01
PADDLE_X0 = 750
PADDLE_Y0 = 200
BALL_Y0 = PADDLE_Y0

PAD_VY = 2
BALL_VX = 5

COLORS = ["blue", "red", "green", "yellow", "brown", "gray"]


# Paddle
@dataclass
class Paddle:
    id: int
    x: int
    y: int
    w: int
    h: int
    vy: int
    c: str


def make_paddle(x, y, w=20, h=100, c="blue"):
    id = canvas.create_rectangle(x, y, x + w, y + h, fill=c, outline=c)
    return Paddle(id, x, y, w, h, 0, c)


def move_paddle(pad):
    pad.y += pad.vy


def redraw_paddle(pad):
    canvas.coords(pad.id, pad.x, pad.y, pad.x + pad.w, pad.y + pad.h)


def change_paddle_color(pad, c="red"):
    canvas.itemconfigure(pad.id, fill=c)
    canvas.itemconfigure(pad.id, outline=c)
    redraw_paddle(pad)


# イベント処理のループに登録するハンドラX3
def up_paddle(event):
    paddle.vy = -PAD_VY


def down_paddle(event):
    paddle.vy = PAD_VY


def stop_paddle(event):
    paddle.vy = 0


# Ball
@dataclass
class Ball:
    id: int
    x: int
    y: int
    d: int
    vx: int
    c: str


def make_ball(x, y, d, vx, c="black"):
    id = canvas.create_rectangle(x, y, x + d, y + d, fill=c, outline=c)
    return Ball(id, x, y, d, vx, c)


def move_ball(ball):
    ball.x += ball.vx


def redraw_ball(ball):
    canvas.coords(ball.id, ball.x, ball.y, ball.x + ball.d, ball.y + ball.d)


# Canvas
tk = Tk()
canvas = Canvas(tk, width=800, height=600, bd=0)
canvas.pack()
tk.update()

paddle = make_paddle(PADDLE_X0, PADDLE_Y0)
ball = make_ball(200, BALL_Y0, 10, BALL_VX)

canvas.bind_all("<KeyPress-Up>", up_paddle)
canvas.bind_all("<KeyPress-Down>", down_paddle)
canvas.bind_all("<KeyRelease-Up>", stop_paddle)
canvas.bind_all("<KeyRelease-Down>", stop_paddle)

# 表示を更新するための無限ループ(イベント処理のループではない点に注意)
while True:
    move_paddle(paddle)
    move_ball(ball)
    if ball.x + ball.vx <= 0:
        ball.vx = -ball.vx  # Refrected by wall
    if ball.x + ball.d >= 800:
        break  # Game is over
    # Hit the paddle ? (パドルの裏判定してないのでパドルの裏にボールが回るとバグります）
    if ball.x + ball.d >= paddle.x and paddle.y <= ball.y <= paddle.y + paddle.h:
        change_paddle_color(paddle, random.choice(COLORS))
        ball.vx = -ball.vx
    #draw image
    redraw_paddle(paddle)
    redraw_ball(ball)
    tk.update()
    time.sleep(DURATION)
