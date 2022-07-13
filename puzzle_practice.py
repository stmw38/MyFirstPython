from tkinter import *
from dataclasses import dataclass


# パネルリスト
@dataclass
class Panel:
    w: int
    h: int


panels = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

for p in [0, 1, 2]:
    for m in [0, 1, 2]:
        break

panel_1 = panels[0][1]
print(panel_1)


