"""
The edit distance between two strings refers to the minimum number
of character insertions, deletions, and substitutions required to
change one string to the other. For example, the edit distance
between “kitten” and “sitting” is three: substitute the “k” for “s”,
substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""
from typing import List


def edit_distance_naive(
    first: str, i: int, f_len: int, second: str, j: int, s_len: int
) -> int:
    """Naive Dynamic Programming Solution
    Operations: insert, delete and substitute
    Time Complexity: O(3^(m+n))
    """
    if i == f_len:
        return s_len - j
    if j == s_len:
        return f_len - i

    if first[i] == second[j]:
        return edit_distance_naive(first, i + 1, f_len, second, j + 1, s_len)

    return 1 + min(
        edit_distance_naive(first, i + 1, f_len, second, j + 1, s_len),  # substitute
        edit_distance_naive(first, i, f_len, second, j + 1, s_len),  # insert
        edit_distance_naive(first, i + 1, f_len, second, j, s_len),  # delete
    )


def edit_distance_dp(first: str, f_len: int, second: str, s_len: int) -> int:
    """More Efficient Dynamic Programming
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    """
    solution: List[List[int]] = [[0] * (s_len + 1) for _ in range(f_len + 1)]

    for i in range(f_len + 1):
        for j in range(s_len + 1):
            if i == 0:
                solution[i][j] = j
            elif j == 0:
                solution[i][j] = i
            elif first[i - 1] == second[j - 1]:
                solution[i][j] = solution[i - 1][j - 1]
            else:
                solution[i][j] = 1 + min(
                    solution[i - 1][j - 1], solution[i][j - 1], solution[i - 1][j]
                )

    return solution[f_len][s_len]


if __name__ == "__main__":
    first_1: str = "kitten"
    f_len_1: int = len(first_1)
    second_1: str = "sitting"
    s_len_1: int = len(second_1)

    first_2: str = "sunday"
    f_len_2: int = len(first_2)
    second_2: str = "saturday"
    s_len_2: int = len(second_2)
    print(
        "edit distance between",
        first_1,
        "and",
        second_1,
        "is:",
        edit_distance_naive(first_1, 0, f_len_1, second_1, 0, s_len_1),
    )
    print(
        "edit distance between",
        first_2,
        "and",
        second_2,
        "is:",
        edit_distance_naive(first_2, 0, f_len_2, second_2, 0, s_len_2),
    )

    print(
        "edit distance between",
        first_1,
        "and",
        second_1,
        "is:",
        edit_distance_dp(first_1, f_len_1, second_1, s_len_1),
    )
    print(
        "edit distance between",
        first_2,
        "and",
        second_2,
        "is:",
        edit_distance_dp(first_2, f_len_2, second_2, s_len_2),
    )
