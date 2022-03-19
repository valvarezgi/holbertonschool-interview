#!/usr/bin/python3
"""modle"""
import sys


def check_pos(solution, position):
    """c"""
    for queen in solution:
        if queen[1] == position[1]:
            return False
        if (queen[0] + queen[1]) == (position[0] + position[1]):
            return False
        if (queen[0] - queen[1]) == (position[0] - position[1]):
            return False
    return True


def move(row, number, solution):
    """m"""
    if (row != number):
        for col in range(number):
            position = [row, col]
            if check_pos(solution, position):
                solution.append(position)
                move(row + 1, number, solution)
                solution.remove(position)
    else:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        number = int(sys.argv[1])
    except BaseException:
        print('N must be a number')
        exit(1)
    if number < 4:
        print('N must be at least 4')
        exit(1)

    solution = []
    row = 0

    move(row, number, solution)
