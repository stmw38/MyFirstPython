import math
import random


class TableManager:
    table: []
    width: int
    height: int

    def __init__(self, w, h):
        self.width = w
        self.height = h
        free_x = math.floor(random.uniform(0, w))  # ０以上w以下
        if free_x >= w:
            free_x = w - 1  # w以上だったら
        free_y = math.floor(random.uniform(0, h))  # ０以上h以下
        if free_y >= h:
            free_y = h - 1  # h以上だったら

        self.table = []
        for x in range(w):
            tmp = []
            for y in range(h):
                if x == free_x and y == free_y:
                    tmp.append(False)
                else:
                    tmp.append(True)
            self.table.append(tmp)

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

# move2freespace(x, y)で、(x, y)の4近傍に移動先が
# あればテーブルを書き換えたうえで移動先の座標
# を示し、移動先がなければx, y自身を返すような
# 動作になります。テーブル上ではFalseの場所が
# 空き状態、Trueの場所が埋まっている状態です
    def move2freespace(self, x_pos, y_pos):
        ret = self.check4neighbor(x_pos, y_pos)
        if ret is None:
            return x_pos, y_pos
        else:
            self.table[x_pos][y_pos] = False
            self.table[ret[0]][ret[1]] = True
            return ret[0], ret[1]


# 以下、動作テスト
tm = TableManager(3, 3)

for y in range(tm.height):
    for x in range(tm.width):
        print(tm.table[x][y], ' ', end='')
    print('')

print('(0, 0) -> ', end="")
ret = tm.move2freespace(0, 0)
print('({}, {})'.format(ret[0], ret[1]))

for y in range(tm.height):
    for x in range(tm.width):
        print(tm.table[x][y], ' ', end='')
    print('')
