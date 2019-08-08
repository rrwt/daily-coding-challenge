"""
There is an N by M matrix of zeroes. Given N and M, write a function to count the number
of ways of starting at the top-left corner and getting to the bottom-right corner.
You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2,
since there are two ways to get to the bottom-right:
    Right, then down
    Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
"""
from typing import Union


def count_ways_recursive(n: int, m: int) -> int:
    """
    """
    if n == 0 or m == 0:
        return 0
    if n == 1 or m == 1:
        return 1

    return count_ways_recursive(n - 1, m) + count_ways_recursive(n, m - 1)


def count_ways_dp(n: int, m: int) -> int:
    """
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    """
    if n == 0 or m == 0:
        return 0

    count_arr: list = [[None] * (m + 1) for _ in range(n + 1)]

    for i in range(m + 1):
        count_arr[1][i] = 1
    for i in range(n + 1):
        count_arr[i][1] = 1

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            count_arr[i][j] = count_arr[i - 1][j] + count_arr[i][j - 1]

    return count_arr[n][m]


def count_ways_combinatorics(n: int, m: int) -> int:
    """
    (m-1 + n-1)!/(m-1)!(n-1)!
    Time Complexity: O(m)
    Space Complexity: O(1)
    """
    res: Union[int, float] = 1
    for i in range(n, m + n - 1):
        res *= i
        res /= i - n + 1

    return int(res)


if __name__ == "__main__":
    n_m_arr, res_arr = [(0, 2), (1, 10), (2, 2), (3, 3), (5, 5)], [0, 1, 2, 6, 70]

    for (n, m), res in zip(n_m_arr, res_arr):
        assert count_ways_recursive(n, m) == res
        assert count_ways_dp(n, m) == res
        assert count_ways_combinatorics(n, m) == res
