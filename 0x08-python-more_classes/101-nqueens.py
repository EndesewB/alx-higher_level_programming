#!/usr/bin/python3
import sys
"""The module to solve n queens"""


def n_queens(n_n):
    """this function is to solve the problem of the n queen chessboard
    Args:
        n_n: the dimension of the chassboard
    Returns: nxn matrix
        """
    if not isinstance(n_n, int):
        print("N must be a number")
        sys.exit(1)
    if n_n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_valid(chessboard, row, colum):
        for i in range(row):
            if chessboard[i] == colum or \
               chessboard[i] - i == colum - row or \
               chessboard[i] + i == colum + row:
                return False
        return True

    def backtrack(chessboard, row):
        if row == n_n:
            print(" ".join(str(chessboard[i] + 1) for i in range(n_n)))
            return
        for colum in range(n_n):
            if is_valid(chessboard, row, colum):
                chessboard[row] = colum
                backtrack(chessboard, row + 1)

    board = [-1] * n_n
    backtrack(board, 0)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

n_queens(n)
