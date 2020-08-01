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
                res, new_total = subset_sum(arr, k, arr_size, res, i + 1, total + arr[i])

                if new_total == k:
                    return res, new_total

                res.pop()  # backtrack

    return res or None, total


def subset_sum_dp(arr: list, k: int, arr_size: int) -> Tuple[bool, Optional[list]]:
    """
    Time Complexity: O(sum * n)
    Space Complexity: O(sum * n)
    """
    dp = [[False] * (k+1) for _ in range(arr_size+1)]

    for _ in range(arr_size+1):
        dp[_][0] = True

    for ind in range(1, arr_size+1):
        for cur_sum in range(1, k+1):
            if cur_sum >= arr[ind-1]:
                # if current sum >= current element, then dp[ind][cur_sum] is true if
                # dp[ind-1[cur_sum] is true - leave current element
                # or dp[ind-1][cur_sum-arr[ind-1]] is true - take current element
                dp[ind][cur_sum] = dp[ind-1][cur_sum] or dp[ind-1][cur_sum-arr[ind-1]]
            else:
                dp[ind][cur_sum] = dp[ind-1][cur_sum]

    if dp[arr_size][k] is False:
        return False, None

    # get the array
    res = []
    ind, cur_sum = arr_size, k

    while cur_sum > 0:
        # reverse the logic from dp construction
        # leave the element part has no impact, therefore do not test for it
        if cur_sum >= arr[ind-1] and dp[ind-1][cur_sum-arr[ind-1]] is True:
            res.append(arr[ind-1])
            cur_sum -= arr[ind-1]
        ind -= 1

    return True, res


if __name__ == "__main__":
    print(*subset_sum([12, 1, 61, 5, 9, 2], 24, 6, []), sep=", ")
    print(subset_sum_dp([12, 1, 61, 5, 9, 2], 24, 6))
    print(subset_sum_dp([2, 3, 7, 8, 10], 11, 5))
