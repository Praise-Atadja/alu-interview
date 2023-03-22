#!/usr/bin/python3
""" Pascal triangle method"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers"""
    first_list = []
    if (n <= 0):
        return first_list
    for i in range(1, (n + 1)):
        second_list = []
        for j in range(i):
            second_list.append(1)
        first_list.append(second_list)
    for i in range(len(first_list)):
        for j in range(i):
            if j != 0:
             first_list[i][j] = first_list[i - 1][j] + first_list[i - 1][j - 1]
    return first_list
