#!/usr/bin/python3
""" The module that performs the chess game problem"""
import sys


def is_valid(chessboard, row, colum):
    """Validating the chessboard with its parameters/chessboard, row and column"""
    for r, c in chessboard:
        if c == colum or r - c == row - colum or r + c == row + colum:
            return False
    return True


def n_queens(n_n, chessboard=[]):
    """creating an empty chessboard
    Args:
        n_n: the dimension of the board
        chessboard: an empty board
    Returns: chessboard
        """
    if len(chessboard) == n_n:
        print(chessboard)
        return
    for colum in range(n_n):
        if is_valid(chessboard, len(chessboard), colum):
            chessboard.append([len(chessboard), colum])
            n_queens(n_n, chessboard)
            chessboard.pop()


if len(sys.argv) != 2:
    """taking the arguments from the user"""
    print("Usage: nqueens N")
    sys.exit(1)

try:
    """Exceptions"""
    nxn = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if nxn < 4:
    print("N must be at least 4")
    sys.exit(1)

n_queens(nxn)
