#TicTacToe_Game

import tkinter as tk
from itertools import cycle
from tkinter import font
from typing import NamedTuple

class Player(NamedTuple):
    label: str
    color: str
    font: str

class Move(NamedTuple):
    row: int
    col: int
    label: str = ""

BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="blue", font="14"),
    Player(label="O", color="red", font="14"),
    )

class TicTacToe_Logic:
    def __init__(self, players = DEFAULT_PLAYERS, board_size = BOARD_SIZE):
        self._players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self._players)
        self.winner_combo = []
        self._current_moves = []
        self._has_winner = False
        self._winning_combos = []
        self._setup_board()

    def _setup_board(self):
        self._current_moves = [
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)]
        self._winning_combos = self._get_winning_combos
        
    def valid_move(self, move):
        row, col = move.row, move.col
        move_was_not_played = self._current_moves[row][col].label == ""
        no_winner = not self._has_winner
        return no_winner and move_was_not_played
    
    def toggle_player(self):
        self.current_player = next(self._players)

    def _get_winning_combos(self):
        rows = [
            [(move.row, move.col) for move in row]
            for row in self._current_moves
        ]
        columns = [list(col) for col in zip(*rows)]
        return rows + columns

class TicTacToe_Board(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.title("TicTacToe 2.0")
        self._cells = {}
        self._game = game
        self._create_board_display()
        self._create_board_grid()

    def _update_button(self, clicked_btn):
        if(clicked_btn['text']=='X' or clicked_btn['text']=='O'):
            clicked_btn.config(text="")
        else:
            clicked_btn.config(text=self._game.current_player.label)
            clicked_btn.config(fg=self._game.current_player.color)
            #clicked_btn.config(font=self._game.current_player.font)

    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="TicTacToe 2.0",
            font=font.Font(size=28, weight="bold"),)
        self.display.pack()

    def _create_board_grid(self):
        for i in range(self._game.board_size):
            
            grid_frameb = tk.Frame(master=self, highlightbackground="black", highlightthickness=1, bd=0)
            grid_frameb.pack(side="left")

            for j in range(self._game.board_size):
                grid_framea = tk.Frame(master=grid_frameb, highlightbackground="black", highlightthickness=1, bd=0)
                grid_framea.pack(side="top")
        
                for row in range(self._game.board_size):
                    self.rowconfigure(row, weight=1, minsize=50)
                    self.columnconfigure(row, weight=1, minsize=50)

                    for col in range(self._game.board_size):
                        button = tk.Button(master=grid_framea, text="", font=font.Font(size=5, weight="bold"), width=8, height=5)
                        self._cells[button] = (row, col)
                        button.grid(row=row, column=col)

                        self._cells[button] = (row, col)
                        button.bind("<ButtonPress-1>", self.play)


    def play(self, event):
        clicked_btn = event.widget
        row, col = self._cells[clicked_btn]
        move = Move(row, col, self._game.current_player.label)
        self._update_button(clicked_btn)
        #self._game.process_move(move)
        self._game.toggle_player()

def main():
    game = TicTacToe_Logic()
    board = TicTacToe_Board(game)
    board.mainloop()

if __name__ == "__main__":
    main()