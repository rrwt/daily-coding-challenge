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

    count_arr: list = [[None] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                count_arr[i][j] = 1
            else:
                count_arr[i][j] = count_arr[i - 1][j] + count_arr[i][j - 1]

    return count_arr[n-1][m-1]


def count_ways_print_all_paths(n: int, m: int) -> int:
    def print_paths(x: int, y: int, ways: list) -> int:
        if x == 0 or y == 0:
            print(ways)
            return 0
        elif x == 1 or y == 1:
            if y > 1:
                z = y
                while z > 1:
                    ways = [(x, z - 1)] + ways
                    z -= 1
            elif x > 1:
                z = x
                while z > 1:
                    ways = [(z - 1, y)] + ways
                    z -= 1

            print(*ways, (n, m), sep=", ")
            return 1
        else:
            return print_paths(x - 1, y, [(x - 1, y)] + ways) + print_paths(
                x, y - 1, [(x, y - 1)] + ways
            )

    print("printing paths for", n, "X", m, "matrix")
    return print_paths(n, m, [])


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

    for (a, b), r in zip(n_m_arr, res_arr):
        assert count_ways_recursive(a, b) == r
        assert count_ways_print_all_paths(a, b) == r
        assert count_ways_dp(a, b) == r
        assert count_ways_combinatorics(a, b) == r
