from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=300)
canvas.pack()


def on_Key_press(event):
    print("key: {}".format(event.keysym))  # 標準出力への出力、{}は%sみたいなもの


canvas.bind_all("<KeyPress>", on_Key_press)

tk.mainloop()
