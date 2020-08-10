"""
Given n dice each with m faces, numbered from 1 to m, find the number of ways to get sum X.
X is the summation of values on each face when all the dice are thrown.
"""


def find_ways(m: int, n: int, x: int) -> int:
    """
    Time Complexity: O(m*n*x)
    Space Complexity: O(n*x
    """
    if x >= m * n:
        return int(x == m * n)
    if x <= n:
        return int(x == n)

    dp = [[0] * (x+1) for _ in range(n+1)]
    dp[0][0] = 1

    for total in range(1, m+1):
        dp[1][total] = 1

    for total in range(1, x+1):
        for dices in range(2, n+1):
            if dices * m < total:
                continue

            for faces in range(1, min(m+1, total)):
                dp[dices][total] += dp[dices-1][total-faces]

    return dp[n][x]


if __name__ == "__main__":
    assert find_ways(4, 2, 1) == 0
    assert find_ways(2, 2, 3) == 2
    assert find_ways(6, 3, 8) == 21
    assert find_ways(4, 2, 5) == 4
    assert find_ways(4, 3, 5) == 6
