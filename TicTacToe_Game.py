#TicTacToe_Game

import tkinter as tk
from itertools import cycle
from tkinter import font
from typing import NamedTuple

class Player(NamedTuple):
    lable: str
    color: str

class Move(NamedTuple):
    row: int
    col: int
    label: str = ""

    BOARD_SIZE = 9
    DEFAULT_PLAYERS = (
        Player(label="X", color="blue"),
        Player(label="O", color="red"),
    )

class TicTacToe_Logic:
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self._players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self._players)
        self._current_moves = []
        self._has_winner = False
        self._setup_board()

class TicTacToe_Board(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TicTacToe 2.0")
        self._cells = {}
        self._create_board_display()
        self._create_board_grid()

    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="TicTacToe 2.0",
            font=font.Font(size=28, weight="bold"),)
        self.display.pack()

    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        
        for row in range(9):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=50)
            for col in range(9):
                button = tk.Button(master=grid_frame, text="", font=font.Font(size=5, weight="bold"), width=8, height=5)
                self._cells[button] = (row, col)
                button.grid(row=row, column=col)

def main():
    board = TicTacToe_Game()
    board.mainloop()

if __name__ == "__main__":
    main()