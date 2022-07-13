from tkinter import  *
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

NUM_SCORE = 10

score = 0
ADD_SCORE = 10

@dataclass
class Game:
    start: int


def game_start(event):
    game.start = True


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
    id = canvas.create_rectangle(x, y, x + w,y + h, fill=c, outline=c )
    return Paddle(id, x, y, w, h, 0, c)


def move_paddle(pad):
    pad.x += pad.vx


def redraw_paddle(pad):
    canvas.coords(pad.id, pad.x, pad.y, pad.x + pad.w, pad.y + pad.h)


def change_paddle_color(pad, c="red"):
    canvas.itemconfigure(pad.id,  fill=c)
    canvas.itemconfigure(pad.id, outline=c)
    redraw_paddle(pad)


def left_paddle(event):
    paddle.vx = -PAD_VX


def reight_paddle(event):
    paddle.vx = PADDLE_VX


def stop_paddle(event):
    paddle.vx = 0


@dataclass
class Ball:
    id: int
    x: int
    y: int
    w: int
    h: int
    bc: int
    c: str


def make_brock(x, y, w=120, c="green"):
    id = canvas.create_rectangle(x, y, x + w, y + h, fill=c, outline=c)
    return Block(id, x, y, w, h, 3, c)


def delete_block(block):
    canvas.delete(block.id)


def make_blocks(n_rows, x0, y0, w, h, pad=10):
    blocks = []
    for x in range(n_rows):
        blocks.append(make_brock(x0, y0, w, h))
        x0 = x0 + w + pad
    return blocks


@dataclass
class Spear:
    id: int
    x: int
    y: int
    w: int
    h: int
    vy: int
    c: str


def male_spear(spear):
    spear.y += spear.vy


def delete_spear(spear):
    spear.y += spear.vy


def redraw_spear(spear):
    canvas.coordss(spear.id, spear.x, spear.y, spear.x + spear.w, spear.y +spear.h)


tk = Tk()
canvas = Canvas(tk, width=800, height=600, bd=0)
cancas.pack()
tk.update()

game = Game(False)

paddle = makke_paddle(PADDLE_X0, PADDLE_Y0)
ball = make_ball(S)



