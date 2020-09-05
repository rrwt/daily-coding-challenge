"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
Example:
    Input: [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
"""
from typing import List


def max_water(elevation: List[int]) -> int:
    size = len(elevation)

    left_largest = [0] * size
    right_largest = [0] * size

    for index in range(1, size):
        left_largest[index] = max(left_largest[index - 1], elevation[index - 1])

    for index in range(size - 2, -1, -1):
        right_largest[index] = max(right_largest[index + 1], elevation[index + 1])

    water = 0
    for index in range(1, size - 1):  # water at index
        water += max(
            0, min(left_largest[index], right_largest[index]) - elevation[index]
        )

    return water


if __name__ == "__main__":
    assert max_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
