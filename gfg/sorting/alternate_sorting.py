"""
Given an array of integers, print the array in such a way that the first element
is first maximum and second element is first minimum and so on
"""


def alternate_sort(arr: list) -> list:
    """
    Time Complexity: O(nlogn)
    Space Complexity: O(n)
    """

    arr.sort()
    i, j, k = 0, len(arr) - 1, 0
    res: list = [None] * (j + 1)

    while k < len(arr):
        res[k] = arr[j]
        k += 1
        j -= 1

        if j > i:
            res[k] = arr[i]
            i += 1
            k += 1

    return res


if __name__ == "__main__":
    arr_list: list = [[7, 1, 2, 3, 4, 5, 6], [1, 6, 9, 4, 3, 7, 8, 2]]

    for arr in arr_list:
        print(alternate_sort(arr))
