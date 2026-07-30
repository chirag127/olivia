"""Tic-Tac-Toe win/tie detection logic (pure, no Tk)."""

import numpy as np

from olivia.games.tic_tac_toe import is_tie, is_winner

X = -1
O = 1


def board(rows):
    return np.array(rows, dtype=float)


def test_row_win_x():
    assert is_winner(board([[X, X, X], [0, 0, 0], [0, 0, 0]]), "X")


def test_column_win_o():
    assert is_winner(board([[O, 0, 0], [O, 0, 0], [O, 0, 0]]), "O")


def test_diagonal_win_x():
    assert is_winner(board([[X, 0, 0], [0, X, 0], [0, 0, X]]), "X")


def test_anti_diagonal_win_o():
    assert is_winner(board([[0, 0, O], [0, O, 0], [O, 0, 0]]), "O")


def test_no_win_empty():
    assert not is_winner(board([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), "X")
    assert not is_winner(board([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), "O")


def test_wrong_player_not_winner():
    # X has a row; O should not be reported as winner.
    b = board([[X, X, X], [0, 0, 0], [0, 0, 0]])
    assert not is_winner(b, "O")


def test_tie_full_board():
    assert is_tie(board([[X, O, X], [X, O, O], [O, X, X]]))


def test_not_tie_with_empty():
    assert not is_tie(board([[X, O, X], [X, 0, O], [O, X, X]]))
