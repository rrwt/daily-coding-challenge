"""
Given an array where difference between adjacent elements is k, write an algorithm to search
for an element in the array and return the position of the element (return the first occurrence).
"""
import random


def search(arr: list, elem: int, max_diff: int) -> int:
    i, l = 0, len(arr)

    while i < l:
        if arr[i] == elem:
            return i
        else:
            j = abs((elem - arr[i]) // max_diff)
            i += j or 1

    return -1


if __name__ == "__main__":
    arr_list: list = [[8, 7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3]]

    for arr in arr_list:
        for elem in [random.choice(arr) for _ in range(3)]:
            print(
                "element",
                elem,
                "found at index",
                search(arr, elem, random.randint(1, len(arr) // 2)),
                "of array",
                arr,
            )

