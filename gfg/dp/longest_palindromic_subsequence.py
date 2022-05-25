"""Longest Palindromic Subsequence

Length of the longest palindromic subsequence. The subsequence doesn't need to be continuous
"""
from typing import Sequence, List


def lps_naive(sequence: str, start: int, end: int) -> int:
    """
    LPS(i, j) = LPS(i+1, j-1) + 2, if sequence[i] == sequence[j] or i+1 == j-1
              = max(LPS(i+1, j), LPS(i, j-1)), if sequence[i] != sequence[j]
    """
    if start > end:
        return 0

    if start == end:
        return 1

    if start == end - 1 and sequence[start] == sequence[end]:
        return 2

    if sequence[start] == sequence[end]:
        return 2 + lps_naive(sequence, start + 1, end - 1)

    return max(lps_naive(sequence, start + 1, end), lps_naive(sequence, start, end - 1))


def lps_tabulated(sequence: str) -> int:
    str_len = len(sequence)
    matrix: Sequence[List[int]] = [[0] * str_len for _ in range(str_len)]

    for index in range(str_len):
        matrix[index][index] = 1

    for num_char in range(2, str_len + 1):
        for i in range(str_len - num_char + 1):
            j = i + num_char - 1

            if sequence[i] == sequence[j]:
                if i == j - 1:
                    matrix[i][j] = 2
                else:
                    matrix[i][j] = 2 + matrix[i + 1][j - 1]
            else:
                matrix[i][j] = max(matrix[i + 1][j], matrix[i][j - 1])

    return matrix[0][str_len - 1]


if __name__ == "__main__":
    assert lps_naive("GEEKSFORGEEKS", 0, 12) == 5
    assert lps_tabulated("GEEKSFORGEEKS") == 5
