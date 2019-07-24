"""
Given an array of integers of size n. Assume ‘0’ as invalid number
and all other as valid number. Convert the array in such a way that
if next valid number is same as current number, double its value and
replace the next number with 0. After the modification, rearrange the
array such that all 0’s are shifted to the end.
"""


def rearrange(arr: list) -> list:
    l, i = len(arr), 0

    while i < l - 1:
        if arr[i] == arr[i + 1]:
            arr[i] *= 2
            arr[i + 1] = 0
            i += 1
        i += 1

    j, k = 0, 0

    while k < l:  # also maintain the original order of non-zero number
        while arr[k] == 0:
            k += 1

        if k < l:
            arr[j], arr[k] = arr[k], arr[j]
            j += 1
            k += 1

    return arr


if __name__ == "__main__":
    assert rearrange([2, 2, 0, 4, 0, 8]) == [4, 4, 8, 0, 0, 0]
    assert rearrange([0, 2, 2, 2, 0, 6, 6, 0, 0, 8]) == [4, 2, 12, 8, 0, 0, 0, 0, 0, 0]
