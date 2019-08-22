"""
Count Number of inversions in an array
"""
from typing import Tuple


def merge(left_arr: list, right_arr: list) -> Tuple[list, int]:
    i, j = 0, 0
    l, m = len(left_arr), len(right_arr)
    res: list = []
    inv: int = 0

    while i < l and j < m:
        if left_arr[i] < right_arr[j]:
            res.append(left_arr[i])
            i += 1
        else:
            res.append(right_arr[j])
            j += 1
            inv += l - i

    if i < l:
        res.extend(left_arr[i:])
    if j < m:
        res.extend(right_arr[j:])

    return res, inv


def inversions(arr: list) -> Tuple[list, int]:
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr, left_inv = inversions(arr[:mid])
        right_arr, right_inv = inversions(arr[mid:])
        merge_arr, merge_inv = merge(left_arr, right_arr)
        return merge_arr, left_inv + right_inv + merge_inv

    return arr, 0


if __name__ == "__main__":
    print(inversions([1, 20, 6, 4, 5]))
