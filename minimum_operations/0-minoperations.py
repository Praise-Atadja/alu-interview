#!/usr/bin/python3
"""
Calculates the fewest number of operations
"""


def minOperations(n):
    mn = 0
    div = 2
    while n > 1:
        while n % div == 0:
            mn += div
            n = int(n / div)
        div += 1
    return mn
