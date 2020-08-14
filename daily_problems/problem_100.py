"""
You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x-1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1, y+1),
    (x-1, y+1),
    (x+1, y-1)

You are given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:
    Input: [(0, 0), (1, 1), (1, 2)]
    Output: 2

It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
"""
from typing import List, Tuple


def min_steps_grid(seq: List[Tuple[int, int]]) -> int:
    steps = 0

    for index in range(len(seq) - 1):
        x1, y1 = seq[index]
        x2, y2 = seq[index + 1]

        # go diagonally towards the destination. It will take min of the two differences
        # then add the diff of two differences to it. traverse horizontally / vertically.
        # in effect, you travel the max of two differences horizontal / vertical
        steps += max(abs(y1 - y2), abs(x1 - x2))

    return steps


if __name__ == '__main__':
    assert min_steps_grid([(0, 0), (1, 1), (1, 2)]) == 2
