"""
Given an array arr[] of size n and integer k such that k <= n.
Find the subarray of size k with least average.
"""
import math
from typing import Tuple, Union


def min_avg(arr: list, k: int) -> Tuple[list, Union[float, int]]:
    """
    Time Complexity: O(n)
    space complexity: O(1)
    """
    avg: Union[int, float] = sum(arr[:k]) / k
    start: int = 0
    end: int = k - 1
    cur_avg = avg

    for index in range(k, len(arr)):
        cur_avg = cur_avg + (arr[index] - arr[index - k]) / k

        if cur_avg < avg:
            avg = cur_avg
            start = index - k + 1
            end = index

    return arr[start : end + 1], avg


if __name__ == "__main__":
    arr_list: list = [[3, 7, 90, 20, 10, 50, 40], [3, 7, 5, 20, -10, 0, 12]]
    k_list: list = [3, 2]

    for arr, k in zip(arr_list, k_list):
        res = min_avg(arr, k)
        print(
            "given",
            arr,
            "and k =",
            k,
            ", the subarray",
            res[0],
            "has the minimum average of",
            res[1],
        )
