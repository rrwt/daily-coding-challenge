"""
Given an array of integers and a number x,
find the smallest subarray with sum greater than the given value.
"""
import sys


def smallest_subarray(arr: list, x: int) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    min_count: int = sys.maxsize
    length: int = len(arr)
    start, end, curr_sum = 0, 1, arr[0]

    while end < length:
        if end < start:
            end = start

        while curr_sum <= x and end < length:
            curr_sum += arr[end]
            end += 1

        while curr_sum > x:
            if end - start < min_count:
                min_count = end - start

            curr_sum -= arr[start]
            start += 1

    return min_count if min_count <= length else -1


if __name__ == "__main__":
    arr_list: list = [
        [1, 4, 45, 6, 0, 19],
        [1, 10, 5, 2, 7],
        [1, 11, 100, 1, 0, 200, 3, 2, 1, 250],
        [1, 2, 4],
    ]
    x_list: list = [51, 9, 280, 8]
    solution: list = [3, 1, 4, -1]

    for arr, x, sol in zip(arr_list, x_list, solution):
        assert smallest_subarray(arr, x) == sol
