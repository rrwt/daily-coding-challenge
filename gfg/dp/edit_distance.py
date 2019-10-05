"""Edit Distance
Given two strings str1 and str2 and below operations that can performed on str1.
Find minimum number of edits (Insert, Remove, Replace) required to convert ‘str1’ into ‘str2’.
"""
from typing import Sequence, List


def edit_distance_naive(
    first: str, index_f: int, len_f: int, second: str, index_s: int, len_s: int
) -> int:
    """
    Time Complexity: Exponential
    """
    if index_f >= len_f and index_s >= len_s:
        return 0
    if index_f >= len_f:
        return len_s - index_s
    if index_s >= len_s:
        return len_f - index_f

    if first[index_f] == second[index_s]:
        return edit_distance_naive(first, index_f + 1, len_f, second, index_s + 1, len_s)

    return 1 + min(
        edit_distance_naive(first, index_f + 1, len_f, second, index_s, len_s),  # delete
        edit_distance_naive(first, index_f, len_f, second, index_s + 1, len_s),  # insert
        edit_distance_naive(first, index_f + 1, len_f, second, index_s + 1, len_s),  # edit
    )


def edit_distance_dp(first: str, second: str) -> int:
    length_f: int = len(first)
    length_s: int = len(second)

    matrix: Sequence[List[int]] = [[0] * (length_s + 1) for _ in range(length_f + 1)]

    for f_ind in range(length_f + 1):
        for s_ind in range(length_s + 1):
            if f_ind == 0:
                matrix[f_ind][s_ind] = s_ind
                continue
            if s_ind == 0:
                matrix[f_ind][s_ind] == f_ind
                continue
            if first[f_ind - 1] == second[s_ind - 1]:
                matrix[f_ind][s_ind] = matrix[f_ind - 1][s_ind - 1]
            else:
                matrix[f_ind][s_ind] = 1 + min(
                    matrix[f_ind - 1][s_ind - 1],  # edit
                    matrix[f_ind - 1][s_ind],  # delete
                    matrix[f_ind][s_ind - 1],  # add
                )

    return matrix[length_f][length_s]


if __name__ == "__main__":
    assert edit_distance_naive("geek", 0, 4, "gesek", 0, 5) == 1
    assert edit_distance_naive("cat", 0, 3, "cut", 0, 3) == 1
    assert edit_distance_naive("sunday", 0, 6, "saturday", 0, 8) == 3

    assert edit_distance_dp("geek", "gesek") == 1
    assert edit_distance_dp("cat", "cut") == 1
    assert edit_distance_dp("sunday", "saturday") == 3
