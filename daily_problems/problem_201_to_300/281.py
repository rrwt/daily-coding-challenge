"""
A wall consists of several rows of bricks of various integer lengths and uniform height.
Your goal is to find a vertical line going from the top to the bottom of the wall that
cuts through the fewest number of bricks. If the line goes through the edge between two bricks,
this does not count as a cut.

For example, suppose the input is as follows, where values in each row represent
the lengths of bricks in that row:
    [[3, 5, 1, 1],
     [2, 3, 3, 2],
     [5, 5],
     [4, 4, 2],
     [1, 3, 3, 3],
     [1, 1, 6, 1, 1]]

The best we can we do here is to draw a line after the eighth brick,
which will only require cutting through the bricks in the third and fifth row.
Given an input consisting of brick lengths for each row such as the one above,
return the fewest number of bricks that must be cut to create a vertical line.
"""
from typing import List


def min_brick_cuts(brick_lengths: List[List[int]]) -> int:
    lengths = []
    row_length = []
    max_length = 0

    for index, row in enumerate(brick_lengths):
        lengths.append(set())
        row_total = 0

        for element in row:
            row_total += element
            lengths[index].add(row_total)

        max_length = max(max_length, row_total)
        row_length.append(row_total)

    min_cuts = len(brick_lengths)

    for cut in range(1, max_length):
        cur_cuts = 0

        for index, row in enumerate(lengths):
            if cut not in row and row_length[index] > cut:
                cur_cuts += 1

        min_cuts = min(min_cuts, cur_cuts)

    return min_cuts


if __name__ == "__main__":
    assert (
        min_brick_cuts(
            [
                [3, 5, 1, 1],
                [2, 3, 3, 2],
                [5, 5],
                [4, 4, 2],
                [1, 3, 3, 3],
                [1, 1, 6, 1, 1],
            ]
        )
        == 2
    )

    assert min_brick_cuts([[1]]) == 1
    assert min_brick_cuts([[1], [1, 2]]) == 0
    assert min_brick_cuts([[1, 2], [1, 2]]) == 0
    assert min_brick_cuts([[3, 2], [1, 2]]) == 0
    assert min_brick_cuts([[4, 2], [2, 1]]) == 0
