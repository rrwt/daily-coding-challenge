"""Pancake Sorting
Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.
"""
from typing import List


def reverse(lst: List[int], i: int, j: int) -> List[int]:
    return lst[:i] + lst[i:j][::-1] + lst[j:]


def get_max_val_index(lst: List[int], start: int, end: int) -> int:
    max_index = start

    for index in range(start + 1, end):
        if lst[index] > lst[max_index]:
            max_index = index

    return max_index


def pancake_sorting(lst: List[int]) -> List[int]:
    size = len(lst)

    while size > 1:
        max_index = get_max_val_index(lst, 0, size)
        lst = reverse(lst, max_index, size)
        size -= 1

    return lst


if __name__ == "__main__":
    assert pancake_sorting([4, 5, 2, 3, 1]) == [1, 2, 3, 4, 5]
