"""
Find the minimum number of coins required to make n cents.
You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
"""
import sys
from typing import List


def min_coins_greedy(cents: int, denominations: List[int]) -> int:
    """
    Greedy Solution.
    Might not work in case of different denominations.
    e.g. denominations of 1, 7 and 10 should return 2 for 14 but it will return 5 here.
    """
    min_coins = 0
    len_d = len(denominations)

    for i in range(len_d - 1, -1, -1):
        while denominations[i] <= cents:
            cents -= denominations[i]
            min_coins += 1

        if cents == 0:
            break

    return min_coins if cents == 0 else None


def min_coins_dp(cents: int, denominations: List[int]) -> int:
    """
    Always optimal.
    Time Complexity: O(n * d)  # total cents * number of denominations
    """
    dp = [[sys.maxsize] * (cents + 1) for _ in range(len(denominations))]

    for i in range(cents + 1):
        if i * denominations[0] <= cents:
            dp[0][i * denominations[0]] = i

    for i_d, den in enumerate(denominations[1:], start=1):
        for val in range(cents + 1):
            if den <= val:
                dp[i_d][val] = min(dp[i_d][val - den] + 1, dp[i_d - 1][val])
            else:
                dp[i_d][val] = dp[i_d - 1][val]

    return dp[-1][-1]


if __name__ == "__main__":
    for c in range(100):
        print(
            f"min coins for {c} being greedy are {min_coins_greedy(c, [1, 5, 10, 25])}"
        )
        print(f"min coins for {c} using dp are {min_coins_dp(c, [1, 5, 10, 25])}")

    assert min_coins_dp(14, [1, 7, 10, 25]) == 2
    assert min_coins_dp(12, [1, 6, 10, 25]) == 2
    assert min_coins_dp(32, [1, 8, 10, 25]) == 4
