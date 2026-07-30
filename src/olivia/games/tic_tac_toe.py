"""Tkinter Tic-Tac-Toe with pure, testable win/tie logic."""

import numpy as np

SIZE_OF_BOARD = 600
SYMBOL_SIZE = (SIZE_OF_BOARD / 3 - SIZE_OF_BOARD / 8) / 2
SYMBOL_THICKNESS = 50
SYMBOL_X_COLOR = "#EE4035"
SYMBOL_O_COLOR = "#0492CF"
GREEN_COLOR = "#7BC043"


def is_winner(board_status, player):
    """True if `player` ('X'->-1, 'O'->1) has three in a row on the 3x3 board."""
    val = -1 if player == "X" else 1
    for i in range(3):
        if board_status[i][0] == board_status[i][1] == board_status[i][2] == val:
            return True
        if board_status[0][i] == board_status[1][i] == board_status[2][i] == val:
            return True
    if board_status[0][0] == board_status[1][1] == board_status[2][2] == val:
        return True
    if board_status[0][2] == board_status[1][1] == board_status[2][0] == val:
        return True
    return False


def is_tie(board_status):
    """True if the board is full."""
    r, _ = np.where(np.array(board_status) == 0)
    return len(r) == 0


class TicTacToe:
    """Two-player Tkinter Tic-Tac-Toe. Click a cell to place a mark."""

    def __init__(self):
        from tkinter import Canvas, Tk

        self.window = Tk()
        self.window.title("Tic-Tac-Toe")
        self.canvas = Canvas(self.window, width=SIZE_OF_BOARD, height=SIZE_OF_BOARD)
        self.canvas.pack()
        self.window.bind("<Button-1>", self.click)
        self.initialize_board()
        self.player_X_turns = True
        self.board_status = np.zeros(shape=(3, 3))
        self.player_X_starts = True
        self.reset_board = False
        self.gameover = False
        self.tie = False
        self.X_wins = False
        self.O_wins = False
        self.X_score = 0
        self.O_score = 0
        self.tie_score = 0

    def mainloop(self):
        self.window.mainloop()

    def initialize_board(self):
        for i in range(2):
            self.canvas.create_line(
                (i + 1) * SIZE_OF_BOARD / 3,
                0,
                (i + 1) * SIZE_OF_BOARD / 3,
                SIZE_OF_BOARD,
            )
            self.canvas.create_line(
                0,
                (i + 1) * SIZE_OF_BOARD / 3,
                SIZE_OF_BOARD,
                (i + 1) * SIZE_OF_BOARD / 3,
            )

    def play_again(self):
        self.initialize_board()
        self.player_X_starts = not self.player_X_starts
        self.player_X_turns = self.player_X_starts
        self.board_status = np.zeros(shape=(3, 3))

    def convert_logical_to_grid_position(self, logical_position):
        logical_position = np.array(logical_position, dtype=int)
        return (SIZE_OF_BOARD / 3) * logical_position + SIZE_OF_BOARD / 6

    def convert_grid_to_logical_position(self, grid_position):
        grid_position = np.array(grid_position)
        return np.array(grid_position // (SIZE_OF_BOARD / 3), dtype=int)

    def is_grid_occupied(self, logical_position):
        return self.board_status[logical_position[0]][logical_position[1]] != 0

    def draw_O(self, logical_position):
        g = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_oval(
            g[0] - SYMBOL_SIZE,
            g[1] - SYMBOL_SIZE,
            g[0] + SYMBOL_SIZE,
            g[1] + SYMBOL_SIZE,
            width=SYMBOL_THICKNESS,
            outline=SYMBOL_O_COLOR,
        )

    def draw_X(self, logical_position):
        g = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_line(
            g[0] - SYMBOL_SIZE,
            g[1] - SYMBOL_SIZE,
            g[0] + SYMBOL_SIZE,
            g[1] + SYMBOL_SIZE,
            width=SYMBOL_THICKNESS,
            fill=SYMBOL_X_COLOR,
        )
        self.canvas.create_line(
            g[0] - SYMBOL_SIZE,
            g[1] + SYMBOL_SIZE,
            g[0] + SYMBOL_SIZE,
            g[1] - SYMBOL_SIZE,
            width=SYMBOL_THICKNESS,
            fill=SYMBOL_X_COLOR,
        )

    def is_winner(self, player):
        return is_winner(self.board_status, player)

    def is_tie(self):
        return is_tie(self.board_status)

    def is_gameover(self):
        self.X_wins = self.is_winner("X")
        if not self.X_wins:
            self.O_wins = self.is_winner("O")
        if not self.O_wins:
            self.tie = self.is_tie()
        return self.X_wins or self.O_wins or self.tie

    def display_gameover(self):
        if self.X_wins:
            self.X_score += 1
            text, color = "Winner: Player 1 (X)", SYMBOL_X_COLOR
        elif self.O_wins:
            self.O_score += 1
            text, color = "Winner: Player 2 (O)", SYMBOL_O_COLOR
        else:
            self.tie_score += 1
            text, color = "Its a tie", "gray"
        self.canvas.delete("all")
        self.canvas.create_text(
            SIZE_OF_BOARD / 2,
            SIZE_OF_BOARD / 3,
            font="cmr 60 bold",
            fill=color,
            text=text,
        )
        score = (
            f"Player 1 (X) : {self.X_score}\n"
            f"Player 2 (O): {self.O_score}\n"
            f"Tie                    : {self.tie_score}"
        )
        self.canvas.create_text(
            SIZE_OF_BOARD / 2,
            3 * SIZE_OF_BOARD / 4,
            font="cmr 30 bold",
            fill=GREEN_COLOR,
            text=score,
        )
        self.reset_board = True

    def click(self, event):
        logical_position = self.convert_grid_to_logical_position([event.x, event.y])
        if not self.reset_board:
            if not self.is_grid_occupied(logical_position):
                if self.player_X_turns:
                    self.draw_X(logical_position)
                    self.board_status[logical_position[0]][logical_position[1]] = -1
                else:
                    self.draw_O(logical_position)
                    self.board_status[logical_position[0]][logical_position[1]] = 1
                self.player_X_turns = not self.player_X_turns
            if self.is_gameover():
                self.display_gameover()
        else:
            self.canvas.delete("all")
            self.play_again()
            self.reset_board = False


def play():
    """Launch the Tic-Tac-Toe window."""
    TicTacToe().mainloop()
