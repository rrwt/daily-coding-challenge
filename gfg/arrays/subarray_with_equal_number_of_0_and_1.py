"""
Given an array containing only 0s and 1s, find the largest subarray
which contain equal no of 0s and 1s.
"""


def subarray(orig_arr: list) -> list:
    """
    Time Complexity: O(n)
    """
    l: int = len(orig_arr)
    left_sum = [-1 if _ == 0 else 1 for _ in orig_arr]

    for i in range(1, l):
        left_sum[i] += left_sum[i - 1]

    hash_table: dict = {}
    start, end = -1, -1

    for i, el in enumerate(left_sum):
        if el == 0 and i > end - start:
            end = i
            start = 0
        elif el not in hash_table:
            hash_table[el] = i
        else:
            if i - hash_table[el] > end - start:
                start = hash_table[el]
                end = i

    return orig_arr[start + 1 : end + 1]


if __name__ == "__main__":
    arr_list: list = [
        [1, 0, 1, 1, 1, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 1, 1, 0],
        [1, 0, 0, 1, 0, 1, 1],
    ]

    for arr in arr_list:
        print(subarray(arr))
