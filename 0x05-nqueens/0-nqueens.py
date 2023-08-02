#!/usr/bin/python3
"""Solving N Queens with Backtracing"""
import sys


def nqueens(n: int):
    """
    Method: nqueens - place n queens
            on an n by n board so that
            no queens are attacking
            others.
    Parameters: n and # of queens
    Return: All possible solutions to
            placement
    """
    matrix = [[0 for x in range(n)] for y in range(n)]
    print(str(matrix))


if __name__ == "__main__":
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print("Usage: nqueens N")
        exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

    nqueens(int(sys.argv[1]))
