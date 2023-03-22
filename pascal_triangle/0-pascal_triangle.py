#!/usr/bin/python3
""" Pascal triangle method"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers"""
    first = []
    if (n <= 0):
        return first
    for i in range(1, (n + 1)):
        second = []
        for j in range(i):
            second.append(1)
        first.append(second)
    for i in range(len(first)):
        for j in range(i):
            if j != 0:
                first[i][j] = first[i - 1][j] + first[i - 1][j - 1]
    return first
