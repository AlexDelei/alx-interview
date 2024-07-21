#!/usr/bin/python3
"""
Rotating a 2D Matrix
"""


N = 3


def rotate_2d_matrix(matrix):
    """
    Rotating a 2-dimensional matrix by
    90-degrees
    """
    for x in range(0, int(N / 2)):

        # Consider elements in group
        # of 4 in current square
        for y in range(x, N-x-1):

            # store current cell in temp variable
            temp = matrix[x][y]

            # move values from left to top
            matrix[x][y] = matrix[N-1-y][x]

            # move values from bottom to left
            matrix[N-1-y][x] = matrix[N-1-x][N-1-y]

            # move values from right to bottom
            matrix[N-1-x][N-1-y] = matrix[y][N-1-x]

            # assign temp to right
            matrix[y][N-1-x] = temp
