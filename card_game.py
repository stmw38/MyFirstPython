import tkinter
import random

CARD_WIDTH = 50
CARD_HEIGHT = 70


class Concrntration:
    def __init__(self, master):
        self.master = master

        self.first_card_id = None
        self.second_card_id = None

        self.width = CARD_WIDTH * 13
        self.height = CARD_HEIGHT * 4

        self.remain_card_ids = []

        self.createWidgets()
        self.createCards()
        self.layoutCards()
        self.setEvents()

    def createWidgets(self):
        self.canvas = tkinter.Canvas(
            self.master,
            width=self.width,
            height=self.height,
            bg="white",
            highlightthickness=0
        )
        self.canvas.pack()

    def createCards(self):
        numbers = [
            "A", "2", "3", "4", "5", "6", "7",
            "8", "9", "10", "J", "Q", "K"
        ]

        self.cards = [number for _ in range(4) for number in numbers]

        random.shuffle(self.cards)

    def layoutCards(self):
        for i, number in enumerate(self.cards):
            h = i % 13
            v = i // 13

            x1 = h * CARD_WIDTH
            x2 = (h + 1) * CARD_WIDTH
            y1 = v * CARD_HEIGHT
            y2 = (v + 1) * CARD_HEIGHT

            self.canvas.create_text(
                x1 + CARD_WIDTH / 2, y1 + CARD_HEIGHT / 2,
                text=number,
                font=("", 40)
            )

            fig_id = self.canvas.create_rectangle(
                x1, y1, x2, y2,
                fill="blue",
                tag=number)

            self.remain_card_ids.append(fig_id)

    def setEvents(self):
        self.canvas.bind("<ButtonPress>", self.selectCard)

    def selectCard(self, event):
        if self.first_card_id is not None and self.second_card_id is not None:
            return

        card_fig_ids = self.canvas.find_closest(event.x, event.y)
        card_fig_id = card_fig_ids[0]

        if not card_fig_id in self.remain_card_ids:
            return

        if card_fig_id == self.first_card_id:
            return

        self.canvas.itemconfig(card_fig_id, fill="")

        if self.first_card_id is None:
            self.first_card_id = card_fig_id
        else:
            self.second_card_id = card_fig_id

            first_number = self.canvas.gettags(self.first_card_id)[0]
            second_number = self.canvas.gettags(self.second_card_id)[0]

            if first_number == second_number:
                self.earnCards()
            else:
                self.canvas.unbind("")
                self.master.after(1000, self.reverseCards)

    def reverseCards(self):
        self.canvas.itemconfig(self.first_card_id, fill="blue")
        self.canvas.itemconfig(self.second_card_id, fill="blue")

        self.first_card_id = None
        self.second_card_id = None

        self.canvas.bind("<ButtonPress>", self.selectCard)

    def earnCards(self):
        self.canvas.itemconfig(self.first_card_id, fill="gray")
        self.canvas.itemconfig(self.second_card_id, fill="gray")

        self.canvas.lower(self.first_card_id, "all")
        self.canvas.lower(self.second_card_id, "all")

        self.remain_card_ids.remove(self.first_card_id)
        self.remain_card_ids.remove(self.second_card_id)

        self.first_card_id = None
        self.second_card_id = None

        if len(self.remain_card_ids) == 0:
            self.canvas.create_text(
                self.width / 2, self.height / 2,
                font=("", 80),
                text="GAME CLEAR!!!",
                fill="red"
            )


app = tkinter.Tk()
Concrntration(app)
app.mainloop()
