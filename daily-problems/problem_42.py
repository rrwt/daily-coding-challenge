"""
Given a list of integers S and a target number k, write a function that
returns a subset of S that adds up to k.
If such a subset cannot be made, then return null.
Integers can appear more than once in the list.
You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24,
return [12, 9, 2, 1] since it sums up to 24.
"""
from typing import Tuple, Optional


def subset_sum(
    arr: list, k: int, arr_size: int, res: list, index: int = 0, total: int = 0
) -> Tuple[Optional[list], int]:
    """
    Using backtracking
    Time Complexity: O(n!)
    Space Complexity: O(n)  # stack
    """
    if total < k:
        for i in range(index, arr_size):
            if total + arr[i] <= k:
                res.append(arr[i])
                res, new_total = subset_sum(
                    arr, k, arr_size, res, i + 1, total + arr[i]
                )

                if new_total == k:
                    return res, new_total

                res.pop()  # backtrack

    return res or None, total


if __name__ == "__main__":
    print(*subset_sum([12, 1, 61, 5, 9, 2], 24, 6, []), sep=", ")
