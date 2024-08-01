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
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with a cell contributing 4 to the perimeter
                perimeter += 4

                # Check the cell above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                # Check the cell below
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                # Check the cell to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                # Check the cell to the right
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1

    return perimeter
