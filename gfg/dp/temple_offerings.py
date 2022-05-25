"""
Consider a devotee wishing to give offerings to temples along a mountain range.
The temples are located in a row at different heights.
Each temple should receive at least one offering.
If two adjacent temples are at different altitudes,
then the temple that is higher up should receive more offerings than the one that is lower down.
If two adjacent temples are at the same height,
then their offerings relative to each other does not matter.
Given the number of temples and the heights of the temples in order,
find the minimum number of offerings to bring.
"""
from typing import List


def min_offerings(heights: List[int]) -> int:
    """
    Get the max increasing sequence on the left and the right side of current index,
    leading upto the current index.
    current index's value would be the max of both + 1.
    """
    length = len(heights)

    if length < 2:
        return length

    left_inc = [0] * length
    right_inc = [0] * length

    for index in range(1, length):
        if heights[index] > heights[index - 1]:
            left_inc[index] = left_inc[index - 1] + 1
        if heights[length - 1 - index] > heights[length - index]:
            right_inc[length - 1 - index] = right_inc[length - index] + 1

    return sum(1 + max(left_inc[index], right_inc[index]) for index in range(length))


def min_offerings_two_pass(heights: List[int]) -> int:
    length = len(heights)

    if length < 2:
        return length

    offerings = [1] * length

    for i in range(1, length):
        # if current height is greater than previous, then this should receive more offerings
        if heights[i] > heights[i - 1]:
            offerings[i] = offerings[i - 1] + 1

    for i in range(length - 2, -1, -1):
        # if current height is greater than the next, then this should receive more offerings
        if heights[i] > heights[i + 1] and offerings[i + 1] >= offerings[i]:
            offerings[i] = offerings[i + 1] + 1

    return sum(offerings)


if __name__ == "__main__":
    assert min_offerings([1, 2, 2]) == 4
    assert min_offerings([1, 4, 3, 6, 2, 1]) == 10
    assert min_offerings_two_pass([1, 2, 2]) == 4
    assert min_offerings_two_pass([1, 4, 3, 6, 2, 1]) == 10
