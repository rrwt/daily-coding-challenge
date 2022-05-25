"""
We can determine how "out of order" an array A is by counting the number of inversions it has.
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j.
That is, a smaller element appears after a larger element.
Given an array, count the number of inversions it has. Do this faster than O(N^2) time.
You may assume each element in the array is distinct.
For example, a sorted list has zero inversions.
The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3).
The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
"""
from typing import Tuple


def merge(left_arr: list, right_arr: list) -> Tuple[list, int]:
    inversions: int = 0
    res: list = []
    i, j, len_left, len_right = 0, 0, len(left_arr), len(right_arr)

    while i < len_left and j < len_right:
        if left_arr[i] <= right_arr[j]:
            res.append(left_arr[i])
            i += 1
        else:
            inversions += len_left - i
            res.append(right_arr[j])
            j += 1

    if i < len_left:
        res.extend(left_arr[i:])
    if j < len_right:
        res.extend(right_arr[j:])

    return res, inversions


def count_inversions(arr: list) -> Tuple[list, int]:
    """Merge sort can be used to count the number of inversions
    Time Complexity: O(n*log(n))
    Space Complexity: O(n)
    """
    l: int = len(arr)
    if l > 1:
        mid = l // 2

        left_arr, inv_left = count_inversions(arr[0:mid])
        right_arr, inv_right = count_inversions(arr[mid:l])
        res_arr, inv_merge = merge(left_arr, right_arr)

        return res_arr, inv_left + inv_right + inv_merge

    return arr, 0


if __name__ == "__main__":
    print(count_inversions([2, 4, 1, 3, 5]))
    print(count_inversions([5, 4, 3, 2, 1]))
