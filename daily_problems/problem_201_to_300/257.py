"""
Given an array of integers out of order, determine the bounds of the smallest
window that must be sorted in order for the entire array to be sorted.
For example, given [3, 7, 5, 6, 9], you should return (1, 3).
"""
import sys
from typing import Tuple, List


def smallest_window(array: List[int]) -> Tuple[int, int]:
    first_index = second_index = -1
    size = len(array)

    for index in range(size - 1):
        if array[index] > array[index + 1]:
            first_index = index
            max_val = array[index]
            break
    else:
        return first_index, second_index

    for index in range(first_index + 1, size):
        if array[index] > max_val > array[index - 1]:
            second_index = index - 1
            max_val = array[index]

    return first_index, second_index


def smallest_window_alt(array: List[int]) -> Tuple[int, int]:
    min_val = sys.maxsize
    max_val = -sys.maxsize
    size = len(array)
    left_index = right_index = -1

    for index in range(size - 1, -1, -1):
        if array[index] < min_val:
            min_val = array[index]
        elif array[index] > min_val:
            left_index = index

    for index in range(size):
        if array[index] > max_val:
            max_val = array[index]
        elif array[index] < max_val:
            right_index = index

    return left_index, right_index


if __name__ == "__main__":
    assert smallest_window([3, 7, 5, 6, 9]) == (1, 3)
    assert smallest_window([1, 2, 3, 7, 5, 6, 4, 8]) == (3, 6)
    assert smallest_window([1, 3, 2, 7, 5, 6, 4, 8]) == (1, 6)
    assert smallest_window_alt([3, 7, 5, 6, 9]) == (1, 3)
    assert smallest_window_alt([1, 2, 3, 7, 5, 6, 4, 8]) == (3, 6)
    assert smallest_window_alt([1, 3, 2, 7, 5, 6, 4, 8]) == (1, 6)
