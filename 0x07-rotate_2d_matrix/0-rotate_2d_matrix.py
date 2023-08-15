#!/usr/bin/python3
"""
Rote 2D Matrix
"""


def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Transpose the matrix
    for a in range(n):
        for b in range(a, n):
            matrix[a][b], matrix[b][a] = matrix[b][a], matrix[a][b]

    # Reverse each row
    for a in range(n):
        matrix[a] = matrix[a][::-1]


# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


rotate_2d_matrix(matrix)

for row in matrix:
    print(row)
