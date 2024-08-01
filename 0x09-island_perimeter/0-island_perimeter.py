#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculating the perimeter of the grid
    Perimeter = rows + columns

    Args:
        grid - a list of integers
    Returns:
        - the computer perimeter
    """
    no_rows = 0
    no_columns = 0

    for _ in grid:
        no_columns += 1
    for _ in grid[0]:
        no_rows += 1

    return (no_rows + no_columns + 1)
