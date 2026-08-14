import tkinter as tk
import random

SIZE = 4
CELL_SIZE = 100
PADDING = 10
BACKGROUND_COLOR = "#bbada0"
EMPTY_COLOR = "#cdc1b4"

class Game2048:
    def __init__(self, root):
        self.root = root
        self.root.title("2048 Game")
        self.score = 0

        self.frame = tk.Frame(root, bg=BACKGROUND_COLOR)
        self.frame.grid()

        self.grid = [[0] * SIZE for _ in range(SIZE)]
        self.cells = []

        for i in range(SIZE):
            row = []
            for j in range(SIZE):
                cell = tk.Label(self.frame, text="", bg=EMPTY_COLOR,
                                width=6, height=3, font=("Arial", 24, "bold"))
                cell.grid(row=i, column=j, padx=PADDING, pady=PADDING)
                row.append(cell)
            self.cells.append(row)

        self.add_random()
        self.add_random()
        self.update_grid()

        self.root.bind("<Key>", self.key_handler)

    def add_random(self):
        empty = [(i, j) for i in range(SIZE)
                 for j in range(SIZE) if self.grid[i][j] == 0]
        if empty:
            i, j = random.choice(empty)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4

    def update_grid(self):
        for i in range(SIZE):
            for j in range(SIZE):
                value = self.grid[i][j]
                self.cells[i][j].config(
                    text=str(value) if value else "",
                    bg=self.get_color(value)
                )

    def get_color(self, value):
        colors = {
            0: EMPTY_COLOR,
            2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
            16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
            128: "#edcf72", 256: "#edcc61", 512: "#edc850",
            1024: "#edc53f", 2048: "#edc22e"
        }
        return colors.get(value, "#3c3a32")

    def compress(self, row):
        new_row = [num for num in row if num != 0]
        new_row += [0] * (SIZE - len(new_row))
        return new_row

    def merge(self, row):
        for i in range(SIZE - 1):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i] *= 2
                row[i + 1] = 0
                self.score += row[i]
        return row

    def move_left(self):
        new_grid = []
        for row in self.grid:
            row = self.compress(row)
            row = self.merge(row)
            row = self.compress(row)
            new_grid.append(row)
        self.grid = new_grid

    def move_right(self):
        self.grid = [row[::-1] for row in self.grid]
        self.move_left()
        self.grid = [row[::-1] for row in self.grid]

    def move_up(self):
        self.grid = list(map(list, zip(*self.grid)))
        self.move_left()
        self.grid = list(map(list, zip(*self.grid)))

    def move_down(self):
        self.grid = list(map(list, zip(*self.grid)))
        self.move_right()
        self.grid = list(map(list, zip(*self.grid)))

    def key_handler(self, event):
        key = event.keysym
        old_grid = [row[:] for row in self.grid]

        if key == "Left":
            self.move_left()
        elif key == "Right":
            self.move_right()
        elif key == "Up":
            self.move_up()
        elif key == "Down":
            self.move_down()

        if self.grid != old_grid:
            self.add_random()
            self.update_grid()

root = tk.Tk()
game = Game2048(root)
root.mainloop()
