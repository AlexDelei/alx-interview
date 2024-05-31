#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Pascal's Triangle Logic
    """
    triangle = []
    if n <= 0:
        triangle = []

    try:
        for i in range(1, n + 1):
            center_numbers = []
            b = 1
            for k in range(1, i + 1):
                center_numbers.append(b)
                b = b * (i - k) // k
            triangle.append(center_numbers)
    except Exception as e:
        print(e)
    return triangle
