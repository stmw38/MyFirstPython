from tkinter import *
from dataclasses import dataclass

import random
import math

PANEL_W = 70
PANEL_H = 70


# キャンバス
tk = Tk()
canvas = Canvas(tk, width=1600, height=1200, bd=0)
canvas.pack()


class Game:
    table: []
    width: int
    height: int

    def __init__(self, w, h):
        self.width = PANEL_W * 3
        self.height = PANEL_H * 3

        free_x = math.floor(random.uniform(0, w))
        if free_x >= w:
            free_x = w - 1
        free_y = math.floor(random.uniform(0, h))
        if free_y >= h:
            free_y = h - 1

        self.table = []
        for x in range(w):
            tmp = []
            for y in range(h):
                if x == free_x and y == free_y:
                    tmp.append(False)
                else:
                    tmp.append(True)
            self.table.append(tmp)

    def make_panels(self):
        numbers = [
            "1", "2", "3", "4", "5", "6", "7", "8", "0"
        ]
        self.panels = [number for _ in range(3) for number in numbers]

        random.shuffle(self.panels)

    def layout_panels(self):
        for i, number in enumerate(self.panels):
            h = i % 3
            v = i // 3

            x1 = h * PANEL_W
            x2 = (h + 1) * PANEL_W
            y1 = v * PANEL_H
            y2 = (v + 1) * PANEL_H

            self.canvas.create_text(x1 + PANEL_W / 2, y1 + PANEL_H / 2, text=number)

    def set_events(self):
        self.canvas.bind("<ButtonPress>", self.select_panel)

    def select_panel(self, pos):
        panel_id = self.canvas.find_closest(pos.x, pos.y)

    def check4neighbor(self, x_pos, y_pos):
        if x_pos > 0:
            if not self.table[x_pos - 1][y_pos]:
                return x_pos - 1, y_pos
        if y_pos > 0:
            if not self.table[x_pos][y_pos - 1]:
                return x_pos, y_pos - 1
        if x_pos < self.width - 1:
            if not self.table[x_pos + 1][y_pos]:
                return x_pos + 1, y_pos
        if y_pos < self.height - 1:
            if not self.table[x_pos][y_pos + 1]:
                return x_pos, y_pos + 1
        return None

    def move2freespace(self, x_pos, y_pos):
        ret = self.check4neighbor(x_pos, y_pos)
        if ret is None:
            return x_pos, y_pos
        else:
            self.table[x_pos][y_pos] = False
            self.table[ret[0]][ret[1]] = True
            return ret[0], ret[1]






