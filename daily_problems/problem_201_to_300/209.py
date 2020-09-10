"""
Write a program that computes the length of the longest common subsequence of three given strings.
For example,
    given "epidemiologist", "refrigeration", and "supercalifragilisticexpialodocious",
    it should return 5, since the longest common subsequence is "eieio".
"""


def lcs(first: str, second: str, third: str) -> int:
    """
    Time Complexity: O(l*m*n)
    Space Complexity: O(l*m*n)
    """
    size_1 = len(first)
    size_2 = len(second)
    size_3 = len(third)

    dp = [[[0] * (size_1 + 1) for _ in range(size_2 + 1)] for _ in range(size_3 + 1)]

    for i in range(1, size_1 + 1):
        for j in range(1, size_2 + 1):
            for k in range(1, size_3 + 1):
                if first[i-1] == second[j-1] and second[j-1] == third[k-1]:
                    dp[k][j][i] = dp[k - 1][j - 1][i - 1] + 1
                else:
                    dp[k][j][i] = max(dp[k][j][i - 1], dp[k][j - 1][i], dp[k - 1][j][i])

    return dp[-1][-1][-1]


if __name__ == "__main__":
    assert (
        lcs("epidemiologist", "refrigeration", "supercalifragilisticexpialodocious")
        == 5
    )
