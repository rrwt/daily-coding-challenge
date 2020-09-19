"""
Given an array of numbers N and an integer k, your task is to
split N into k partitions such that the maximum sum of any
partition is minimized. Return this sum.

For example,
    given N = [5, 1, 2, 7, 3, 4] and k = 3, you should return 8,
    since the optimal partition is [5, 1, 2], [7], [3, 4].
"""
import sys
from typing import List


def _partition(array: List[int], index: int, n: int, k: int) -> List[List[int]]:
    if k == 1:
        return [array[index:]]

    min_sum = sys.maxsize
    partitions = []

    for j in range(index + 1, n):
        parts = _partition(array, j, n, k - 1)

        if parts:
            cur_max = max(max(sum(_) for _ in parts), sum(array[index: j]))

            if cur_max < min_sum:
                min_sum = cur_max
                partitions = [array[index:j]] + parts

    return partitions


def partition_recursive(array: List[int], n: int, k: int) -> int:
    partitions = _partition(array, 0, n, k)
    print(f"partitions: {partitions}")
    return max(sum(_) for _ in partitions)


def partition_dp(array: List[int], n: int, k: int) -> int:
    """
    Time Complexity: O(K * N * N)
    Space Complexity: O(K * N)
    """
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    # k = 1
    dp[1][1] = array[0]
    for i in range(1, n):
        array[i] += array[i - 1]  # reusing for sum array
        dp[1][i + 1] = array[i]

    # n = 1
    for i in range(1, k + 1):
        dp[i][1] = array[0]

    for parts in range(2, k + 1):
        for i in range(2, n + 1):
            min_val = sys.maxsize

            for j in range(1, i):
                min_val = min(min_val, max(dp[parts - 1][j], array[i - 1] - array[j - 1]))

            dp[parts][i] = min_val

    return dp[k][n]


if __name__ == "__main__":
    assert partition_recursive([5, 1, 2, 7, 3, 4], 6, 3) == 8
    assert partition_dp([5, 1, 2, 7, 3, 4], 6, 3) == 8
