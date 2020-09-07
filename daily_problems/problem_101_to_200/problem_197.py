"""
Given an array and a number k that's smaller than the length of the array,
rotate the array to the right k elements in-place.
"""
from typing import List


def rotate_arr(arr: List[int], k: int) -> List[int]:
    length = len(arr)
    visited = set()

    for i in range(min(k, length - k)):
        if i in visited:
            continue

        val = arr[i]
        j = (i + k) % length

        while j != i:
            visited.add(j)
            arr[j], val = val, arr[j]
            j = (j + k) % length

        arr[j] = val
        visited.add(j)

    return arr


if __name__ == "__main__":
    assert rotate_arr([1, 2, 3, 4, 5], 1) == [5, 1, 2, 3, 4]
    assert rotate_arr([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate_arr([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2]
    assert rotate_arr([1, 2, 3, 4, 5], 4) == [2, 3, 4, 5, 1]
    assert rotate_arr([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
    assert rotate_arr([1, 2, 3, 4, 5, 6], 2) == [5, 6, 1, 2, 3, 4]
