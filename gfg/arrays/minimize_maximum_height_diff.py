"""
Given heights of n towers and a value k. We need to either increase
or decrease height of every tower by k (only once) where k > 0.
The task is to minimize the difference between the heights of the longest
and the shortest tower after modifications, and output this difference.
"""
from typing import Tuple


def minimize_range(arr: list, k: int) -> Tuple[list, int]:
    """
    Find the max and min element present in the array.
    Check whether the difference between the max and min element is less than or equal to k:
        If yes, then return the difference between the max and min element.
        otherwise go to step 3.
    Calculate the average of the max and min element of the array.
    Traverse the array and do the following operations:
        If the array element is greater than the average then decrease it by k.
        If the array element is smaller than the average then increase it by k.
    Return the difference between the max and min element of the modified array.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def get_min_max(elements: list) -> Tuple[int, int]:
        nonlocal l
        smallest, largest = min(arr[0], arr[1]), max(arr[0], arr[1])
        for index in range(2, l):
            if arr[index] < smallest:
                smallest = arr[index]
            elif arr[index] > largest:
                largest = arr[index]

        return smallest, largest

    l: int = len(arr)
    min_el, max_el = get_min_max(arr)

    diff: int = max_el - min_el

    if diff <= k:
        # it's best to move in the same direction
        arr = [elem + k for elem in arr]
    else:
        avg: float = (min_el + max_el) / 2

        for i in range(l):
            if arr[i] < avg:
                arr[i] += k
            else:
                arr[i] -= k

        min_el, max_el = get_min_max(arr)

    return arr, max_el - min_el


if __name__ == "__main__":
    arr_list: list = [
        [1, 15, 10],
        [1, 5, 15, 10],
        [4, 6],
        [6, 10],
        [1, 10, 14, 14, 14, 15],
        [1, 2, 3],
    ]
    k_list: list = [6, 3, 10, 3, 6, 2]

    for arr, k in zip(arr_list, k_list):
        print("input:", arr, k)
        print("output:", *minimize_range(arr, k))
