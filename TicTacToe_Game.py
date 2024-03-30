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
    def __init__(self, players = DEFAULT_PLAYERS, board_size = BOARD_SIZE):
        self._players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self._players)
        self.winner_combo = []
        self._current_moves = []
        self._has_winner = False
        self._setup_board()

    def _setup_board(self):
        self._current_moves = [
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)]
        
    def valid_move(self, move):
        row, col = move.row, move.col
        move_was_not_played = self._current_moves[row][col].label == ""
        no_winner = not self._has_winner
        return no_winner and move_was_not_played
    
    def toggle_player(self):
        self.current_player = next(self._players)

class TicTacToe_Board(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.title("TicTacToe 2.0")
        self._cells = {}
        self._game = game
        self._create_board_display()
        self._create_board_grid()

    def _update_button(self, clicked_btn):
        clicked_btn.config(text=self._game.current_player.label)
        clicked_btn.config(fg=self._game.current_player.color)

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
        
        for row in range(self._game.board_size):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=50)
            for col in range(self._game.board_size):
                button = tk.Button(master=grid_frame, text="", font=font.Font(size=5, weight="bold"), width=8, height=5)
                self._cells[button] = (row, col)
                button.grid(row=row, column=col)

                self._cells[button] = (row, col)
                button.bind("<ButtonPress-1>", self.play)

    def play(self, event):
        clicked_btn = event.widget
        row, col = self._cells[clicked_btn]
        move = Move(row, col, self._game.current_player.label)
        if self._game.is_valid_move(move):
            self._update_button(clicked_btn)
            self._game.process_move(move)
            self._game.toggle_player()

def main():
    board = TicTacToe_Board()
    board.mainloop()

if __name__ == "__main__":
    main()