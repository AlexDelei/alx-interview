#!/usr/bin/env python3
"""
The N queens puzzle
"""
import sys


def is_safe(board: list[int], row: int, col: int) -> bool:
    """
    Check if it's safe to place a queen at board[row][col]
    This function is called when "col" queens are already
    placed in columns from 0 to col - 1. We just need
    to check the left side for attacking queens.
    """
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solve_nqueens_recursive(
        board: list[int], col: int, n: int
        ) -> list[list[int]]:
    """
    Use backtracking to find all solutions
    """
    if col == n:
        # All queens are placed successfully
        return [[[i, board[i]] for i in range(n)]]

    solutions = []
    for i in range(n):
        if is_safe(board, i, col):
            board[col] = i
            for solution in solve_nqueens_recursive(board, col + 1, n):
                solutions.append(solution)
    return solutions


def solve_nqueens(n: int) -> list[list[int]]:
    """
    Solving the Nqueens puzzle challenge of
    placing N non-attacking queens on an N x N
    puzzle
    """
    board = [-1] * n
    return solve_nqueens_recursive(board, 0, n)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1].rstrip("'"))
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)
