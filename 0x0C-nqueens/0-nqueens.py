#!/usr/bin/python3
"""program that solves N queens puzzle"""
import sys


def get_n():
    """validates command line input"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def row_has_queen(board, row):
    """check row for other queens"""
    for has_queen in board[row]:
        if has_queen:
            return True
    return False


def col_has_queen(board, col):
    """check col for other queens"""
    n = len(board[0])
    for row in range(n):
        has_queen = board[row][col]
        if has_queen:
            return True
    return False


def diag_has_queen(board, row, col):
    """check diagonals for queens"""
    n = len(board[0])

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return True

    for i, j in zip(range(row, -1, -1), range(col, n, 1)):
        if board[i][j]:
            return True

    return False


def print_board(board, n):
    """prints the board"""
    queens = [[i, j] for i in range(n) for j in range(n) if board[i][j]]
    print(queens)


def n_queens():
    """make board"""
    n = get_n()
    board = [[False for j in range(n)] for i in range(n)]
    solve_nqueens(0, 0, board)


def solve_nqueens(idx, queens_found, board):
    """recursive backtracking"""
    n = len(board[0])
    a = False

    if idx >= n ** 2:
        return False

    i, j = [(j, i) for j in range(n) for i in range(n)][idx]

    if not row_has_queen(board, i) and not col_has_queen(board, j) \
       and not diag_has_queen(board, i, j):
        b_true = [row[:] for row in board]
        b_true[i][j] = True

        if queens_found + 1 == n:
            print_board(b_true, n)
            return True

        a = solve_nqueens(idx + 1, queens_found + 1, b_true)

    b_false = [row[:] for row in board]
    b_false[i][j] = False
    b = solve_nqueens(idx + 1, queens_found, b_false)

    if a or b:
        return True


if __name__ == "__main__":
    n_queens()
