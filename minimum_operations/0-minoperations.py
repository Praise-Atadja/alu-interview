#!/usr/bin/python3
"""
A method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
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
