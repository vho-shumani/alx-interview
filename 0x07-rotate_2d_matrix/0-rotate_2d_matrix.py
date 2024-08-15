#!/usr/bin/env python3
"""0-rotate_2d_matrix.py
"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degees clockwise

       Args:
        matrix(list): matrix to rotate
    """
    for row in range(len(matrix)):
        for col in range(row, len(matrix)):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    for row in matrix:
        row.reverse()
