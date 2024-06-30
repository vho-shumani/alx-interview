#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    """
    triangle_list = []
    if n <= 0:
        return triangle_list

    for i in range(n):
        row_list = [1] * (i + 1)
        for j in range(1, i):
            row_list[j] = triangle_list[i - 1][j - 1] + triangle_list[i - 1][j]
        triangle_list.append(row_list)
    return triangle_list
