#!/usr/bin/python3
"""The N queen Puzzle Module"""
import sys
from typing import List


def is_safe(board: List[List[int]], row: int, col: int) -> bool:
    """Check for existence of queen"""
    for i, j in board:
        if j == col or \
           i - j == row - col or \
           i + j == row + col:
            return False
    return True


def solve_n_queens(board: List[List[int]], row: int, n: int) -> None:
    """Solves puzzle"""
    if row == n:
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append([row, col])
            solve_n_queens(board, row + 1, n)
            board.pop()


def main() -> None:
    """The main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if sys.argv[1].isnumeric():
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            exit(1)
        else:
            board = []
            solve_n_queens(board, 0, n)
    else:
        print("N must be a number")
        exit(1)


if __name__ == "__main__":
    main()
