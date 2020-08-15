"""
Given a multiset of integers,
return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10},
it would return true, since we can split it up into 
{15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false,
since we can't split it up into two subsets that add up to the same sum.
"""
from typing import Tuple


def split_arr(
    arr: list, arr_len: int, ind: int, arr1: list, arr2: list
) -> Tuple[bool, list, list]:
    """
    Backtrack. One by one add each array element to either arr1 or arr2
    """
    if ind == arr_len:
        return (True, arr1, arr2) if sum(arr1) == sum(arr2) else (False, arr1, arr2)
    else:
        res = split_arr(arr, arr_len, ind + 1, arr1 + [arr[ind]], arr2)

        return (
            res
            if res[0] is True
            else split_arr(arr, arr_len, ind + 1, arr1, arr2 + [arr[ind]])
        )


def subset_sum(arr: list, arr_len: int, total: int) -> Tuple[bool, list, list]:
    """
    Dynamic Programming
    """
    dp = [[False] * (total + 1) for _ in range(arr_len + 1)]

    for index in range(1, arr_len + 1):
        dp[index][0] = True

        for cur_total in range(1, total + 1):
            if cur_total >= arr[index - 1]:
                dp[index][cur_total] = (
                    dp[index - 1][cur_total]
                    or dp[index - 1][cur_total - arr[index - 1]]
                )
            else:
                dp[index][cur_total] = dp[index - 1][cur_total]

    if not dp[arr_len][total]:
        return False, [], []

    index = arr_len
    cur_total = total
    res1_ind = set()  # get index of elements for first array

    while cur_total > 0 and index > 0:
        if cur_total >= arr[index - 1] and dp[index - 1][cur_total - arr[index - 1]]:
            res1_ind.add(index - 1)
            cur_total -= arr[index - 1]
        index -= 1

    res1, res2 = [], []

    for index, element in enumerate(arr):
        if index in res1_ind:
            res1.append(element)
        else:
            res2.append(element)

    return True, res1, res2


def can_split(arr: list) -> bool:
    arr_len: int = len(arr)

    if sum(arr) % 2 or arr_len < 2:  # sum must be even
        return False

    res, arr1, arr2 = split_arr(arr, arr_len, 0, [], [])  # backtrack

    if res:
        print("The partitioned arrays for", arr, "are:", arr1, "and", arr2)

    res, arr1, arr2 = subset_sum(arr, arr_len, sum(arr) // 2)  # dp

    if res:
        print(f"The partitioned array using dp for {arr} are {arr1} and {arr2}")

    return res


if __name__ == "__main__":
    s1, s2 = [15, 5, 20, 10, 35, 15, 10], [15, 5, 20, 10, 35]
    print("The array", s1, "can" if can_split(s1) else "cannot", "be split in two")
    print("The array", s2, "can" if can_split(s2) else "cannot", "be split in two")
