"""
You are given an array of integers, where each element represents
the maximum number of steps that can be jumped going forward from
that element. Write a function to return the minimum number of jumps
you must take in order to get from the start to the end of the array.

For example,
    given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2,
    as the optimal solution involves jumping from 6 to 5, and then from 5 to 9.
"""
from typing import List


def min_jumps(array: List[int]) -> int:
    size = len(array)

    if size <= 1:
        return 0
    if array[0] == 0:
        return -1

    jumps = 1
    index = 0
    steps = max_reach = array[0]

    while index < size - 1:
        max_reach = max(max_reach, index + array[index])

        if steps == 0:
            jumps += 1
            steps = max_reach - index

        if max_reach >= size - 1:
            return jumps + 1

        steps -= 1
        index += 1

        if index > max_reach:
            return -1

    return -1


if __name__ == "__main__":
    assert min_jumps([6, 2, 4, 0, 5, 1, 1, 4, 2, 9]) == 2
    assert min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]) == 3
