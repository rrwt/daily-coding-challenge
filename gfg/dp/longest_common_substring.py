"""Longest Common Substring
Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order,
but not necessarily contiguous.
"""
from typing import List


def lcs_naive(first: str, index_f: int, second: str, index_s: int) -> int:
    """
    Time Complexity: O(2^n)
    """
    if index_f < 0 or index_s < 0:
        return 0

    if first[index_f] == second[index_s]:
        return 1 + lcs_naive(first, index_f - 1, second, index_s - 1)

    return max(
        lcs_naive(first, index_f - 1, second, index_s),
        lcs_naive(first, index_f, second, index_s - 1),
    )


def lcs_tabulated(first: str, second: str) -> int:
    """
    Time Complexity: O(n*n)
    """
    len_f: int = len(first)
    len_s: int = len(second)

    matrix: List[List[int]] = [[0] * (len_s + 1) for _ in range(len_f + 1)]

    for f in range(1, len_f + 1):
        for s in range(1, len_s + 1):
            if first[f - 1] == second[s - 1]:
                matrix[f][s] = matrix[f - 1][s - 1] + 1
            else:
                matrix[f][s] = max(matrix[f - 1][s], matrix[f][s - 1])

    return matrix[len_f][len_s]


if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    assert lcs_naive(X, len(X) - 1, Y, len(Y) - 1) == 4
    assert lcs_tabulated(X, Y) == 4
