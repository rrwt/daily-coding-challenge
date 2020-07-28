"""
You are given an array of non-negative integers that represents a two-dimensional
elevation map where each element is unit-width wall and the integer is the height.
Suppose it will rain and all spots between two walls get filled up.
Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example
given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index,
2 in the second, and 3 in the fourth index, so we can trap 8 units of water.
"""
from typing import List


def trapped_water(elevations: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    count_el: int = len(elevations)
    max_left = [0] * count_el
    max_right = [0] * count_el
    water_trapped = 0

    for index in range(1, count_el-1):
        max_left[index] = max(max_left[index-1], elevations[index-1])

    for index in range(count_el-2, 0, -1):
        max_right[index] = max(max_right[index+1], elevations[index+1])

    for index, elevation in enumerate(elevations):
        water_trapped += max(min(max_left[index], max_right[index]) - elevation, 0)

    return water_trapped


# TODO O(n) and O(1)


if __name__ == "__main__":
    assert trapped_water([2, 1, 2]) == 1
    assert trapped_water([3, 0, 1, 3, 0, 5]) == 8
