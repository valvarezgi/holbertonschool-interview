#!/usr/bin/python3
"""Minimum Operations module
"""


def minOperations(n):
    """Calculates the fewest number of operations needed to result
    in exactly n H characters
    Args:
        n (int): amount of H
    Return:
        minimum number of operations (an integer)
    """
    numberOfMinOp, div = 0, 2
    while isinstance(n, int) and n > 1:
        while n % div:
            div += 1
        numberOfMinOp += div
        n = int(n / div)
    return numberOfMinOp