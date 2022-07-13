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

BLOCK_X = 10
BLOCK_Y = 160
BLOCK_W = 40
BLOCK_H = 120

NUM_BLOCKS = 4

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


# Block
@dataclass
class Block:
    id: int
    x: int
    y: int
    w: int
    h: int
    c: str


def make_block(x, y, w=40, h=120, c="green"):
    id = canvas.create_rectangle(x, y, x+w, y+h, fill=c, outline=c)
    return Block(id, x, y, w, h, c)


def delete_block(block):
    canvas.delete(block.id) # オブジェクトを消す処理は初出


def make_blocks(n_rows, x0, y0, w, h, pad=10):
    blocks = []
    for x in range(n_rows):
        blocks.append(make_block(x0, y0, w, h))
        x0 = x0 + w + pad
    return blocks


# Wall
def make_walls(ox, oy, width, height):
    canvas.create_rectangle(ox, oy, ox + width, oy + height)
    # オブジェクトを管理する必要がないので戻り値はなし

# Canvas
tk = Tk()
canvas = Canvas(tk, width=800, height=600, bd=0)
canvas.pack()
tk.update()

paddle = make_paddle(PADDLE_X0, PADDLE_Y0)
ball = make_ball(200, BALL_Y0, 10, BALL_VX)
make_walls(0, 0, 800, 600) #
# block = make_block(BLOCK_X, BLOCK_Y, BLOCK_W, BLOCK_H) #
blocks = make_blocks(NUM_BLOCKS, BLOCK_X, BLOCK_Y, BLOCK_W, BLOCK_H)

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

    # Hitting the paddle ? (パドルの裏判定してないのでパドルの裏にボールが回るとバグります）
    if ball.x + ball.d >= paddle.x and paddle.y <= ball.y <= paddle.y + paddle.h:
        change_paddle_color(paddle, random.choice(COLORS))
        ball.vx = -ball.vx

    # Breaking a wall
    for block in blocks:
        if block != None and ball.x <= block.x + block.w and block.y <= ball.y <= block.y + block.h:
            ball.vx = -ball.vx
            delete_block(block)
            blocks.remove(block)
            break

    if not blocks: break # 表示更新のループから脱出->終了

    #draw image
    redraw_paddle(paddle)
    redraw_ball(ball)
    tk.update()
    time.sleep(DURATION)
