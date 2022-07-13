from tkinter import *
from dataclasses import dataclass
import time
import random

DURATION = 0.01
PADDLE_X0 = 400
PADDLE_Y0 = 450
BALL_X0 = PADDLE_X0

PAD_VX = 5
BALL_VX = 3
BALL_VY = 2

COLORS = ["blue", "red", "green", "yellow", "brown", "gray"]

BLOCK_X = 100
BLOCK_Y = 100
BLOCK_W = 120
BLOCK_H = 40

NUM_BLOCKS = 4


# Game Controll
@dataclass
class Game:
    start: int


def game_start(event):
    game.start = True


# Paddle
@dataclass
class Paddle:
    id: int
    x: int
    y: int
    w: int
    h: int
    vx: int
    c: str


def make_paddle(x, y, w=100, h=20, c="blue"):
    id = canvas.create_rectangle(x, y, x + w, y + h, fill=c, outline=c)
    return Paddle(id, x, y, w, h, 0, c)


def move_paddle(pad):
    pad.x += pad.vx


def redraw_paddle(pad):
    canvas.coords(pad.id, pad.x, pad.y, pad.x + pad.w, pad.y + pad.h)


def change_paddle_color(pad, c="red"):
    canvas.itemconfigure(pad.id, fill=c)
    canvas.itemconfigure(pad.id, outline=c)
    redraw_paddle(pad)


# イベント処理のループに登録するハンドラX3
def left_paddle(event):
    paddle.vx = -PAD_VX


def right_paddle(event):
    paddle.vx = PAD_VX


def stop_paddle(event):
    paddle.vx = 0


# Ball
@dataclass
class Ball:
    id: int
    x: int
    y: int
    d: int
    vx: int
    vy: int
    c: str


def make_ball(x, y, d, vx, vy, c="black"):
    id = canvas.create_oval(x, y, x + d, y + d, fill=c, outline=c)
    return Ball(id, x, y, d, vx, vy, c)


def move_ball(ball):
    ball.x += ball.vx
    ball.y += ball.vy


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


def make_block(x, y, w=120, h=40, c="green"):
    id = canvas.create_rectangle(x, y, x + w, y + h, fill=c, outline=c)
    return Block(id, x, y, w, h, c)


def delete_block(block):
    canvas.delete(block.id)  # オブジェクトを消す処理は初出


def make_blocks(n_rows, x0, y0, w, h, pad=10):
    blocks = []
    for x in range(n_rows):
        blocks.append(make_block(x0, y0, w, h))
        x0 = x0 + w + pad
    return blocks


# Canvas
tk = Tk()
canvas = Canvas(tk, width=800, height=600, bd=0)
canvas.pack()
tk.update()

game = Game(False)  # Gameの要素は1つだけなので引数も1つ

paddle = make_paddle(PADDLE_X0, PADDLE_Y0)
ball = make_ball(BALL_X0, 50, 10, BALL_VX, BALL_VY)
blocks = make_blocks(NUM_BLOCKS, BLOCK_X, BLOCK_Y, BLOCK_W, BLOCK_H)

canvas.bind_all("<KeyPress-space>", game_start)
canvas.bind_all("<KeyPress-Left>", left_paddle)
canvas.bind_all("<KeyPress-Right>", right_paddle)
canvas.bind_all("<KeyRelease-Left>", stop_paddle)
canvas.bind_all("<KeyRelease-Right>", stop_paddle)

# Spaceキーの入力待ち
id_text = canvas.create_text(400, 200, text="Press 'Space' to start", font=('FixedSys', 16))
tk.update()

while not game.start:
    tk.update()
    time.sleep(DURATION)

canvas.delete(id_text)
tk.update()

while True:
    move_paddle(paddle)
    move_ball(ball)
    if ball.x + ball.vx <= 0 or ball.x + ball.vx >= 800:
        ball.vx = -ball.vx
    if ball.y + ball.vy <= 0:
        ball.vy = -ball.vy
    if ball.y + ball.d >= 600:
        canvas.create_text(360, 200, text="Game is over...", font=('FixedSys', 16))
        tk.update()
        time.sleep(3)
        break  # Game is over

    # Hitting the paddle ちょっと変更
    if paddle.x <= ball.x + ball.d and ball.x <= paddle.x + paddle.w:
        if ball.y + ball.d <= paddle.y <= ball.y + ball.d + ball.vy:
            change_paddle_color(paddle, random.choice(COLORS))
            ball.vy = -ball.vy
            ball.vx = ((ball.x - paddle.x) - paddle.w / 2) * BALL_VX / paddle.w

    # Breaking a wall
    for block in blocks:
        if block is not None \
                and block.x <= ball.x + ball.d \
                and ball.x <= block.x + block.w \
                and block.y <= ball.y + ball.d \
                and ball.y <= block.y + block.h:
            ball.vy = -ball.vy
            delete_block(block)
            blocks.remove(block)
            break

    if not blocks:
        canvas.create_text(400, 200, text="Clear!", font=('FixedSys', 16))
        tk.update()
        time.sleep(3)
        break  # 表示更新のループから脱出->終了

    # draw image
    redraw_paddle(paddle)
    redraw_ball(ball)
    tk.update()
    time.sleep(DURATION)
