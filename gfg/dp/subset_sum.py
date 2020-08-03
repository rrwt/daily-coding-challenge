"""
Given a set of non-negative integers, and a value sum,
determine if there is a subset of the given set with sum equal to given sum.

Example:
    Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
    Output: True
    There is a subset (4, 5) with sum 9.

    Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
    Output: False
    There is no subset that add up to 30.
"""


def subset_sum(values: list, total: int) -> bool:
    size = len(values)
    dp = [[False] * (total+1) for _ in range(size+1)]

    for index in range(1, size + 1):
        dp[index][0] = True
        for cur_sum in range(1, total+1):
            if cur_sum >= values[index-1]:
                dp[index][cur_sum] = dp[index-1][cur_sum] or dp[index-1][cur_sum-values[index-1]]
            else:
                dp[index][cur_sum] = dp[index-1][cur_sum]

    return dp[size][total]


if __name__ == "__main__":
    for arr, k in ([(3, 34, 4, 12, 5, 2), 9], [(3, 34, 4, 12, 5, 2), 30]):
        print(
            f"subset sum for array: {arr} and total: {k},",
            "exists" if subset_sum(arr, k) else "does not exist"
        )
