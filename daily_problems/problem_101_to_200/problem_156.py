"""
Given a positive integer n, find the smallest number of squared integers which sum to n.
For example, given n = 13, return 2 since 13 = 32 + 22 = 9 + 4.
Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9.
"""


def min_squared_values_naive(n: int) -> int:
    if n < 1:
        return 0

    count_min = n

    for i in range(1, n):
        if i * i > n:
            break
        else:
            count_min = min(count_min, 1 + min_squared_values_naive(n - i * i))

    return count_min


def min_squared_dp(n: int) -> int:
    """
    Time Complexity: O(n * n)
    Space Complexity: O(n)
    """
    dp = [n] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        for j in range(2, i):
            if (val := j * j) <= i:
                dp[i] = min(dp[i - val] + 1, dp[i])
            else:
                break

    return dp[n]


if __name__ == "__main__":
    assert min_squared_values_naive(2) == 2
    assert min_squared_dp(2) == 2
    assert min_squared_values_naive(3) == 3
    assert min_squared_dp(3) == 3
    assert min_squared_values_naive(4) == 1
    assert min_squared_dp(4) == 1
    assert min_squared_values_naive(13) == 2
    assert min_squared_dp(13) == 2
    assert min_squared_values_naive(27) == 3
    assert min_squared_dp(27) == 3
    assert min_squared_values_naive(25) == 1
    assert min_squared_dp(25) == 1
