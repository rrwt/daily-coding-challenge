"""
Given an array of positive integers. We need to make the given
array a ‘Palindrome’. Only allowed operation on array is merge.
Merging two adjacent elements means replacing them with their sum.
The task is to find minimum number of merge operations required
to make given array a ‘Palindrome’.
"""


def count_to_palindrome(arr: list) -> int:
    """
    Time Complexity: O(n)
    """

    i, j = 0, len(arr) - 1
    total: int = 0

    while i < j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
            continue
        elif arr[i] < arr[j]:
            i += 1
            arr[i] += arr[i - 1]
        else:
            j -= 1
            arr[j] += arr[j + 1]

        total += 1

    return total


if __name__ == "__main__":
    arr_list: list = [[15, 4, 15], [1, 4, 5, 1], [11, 14, 15, 99]]
    res_list: list = [0, 1, 3]

    for arr, res in zip(arr_list, res_list):
        assert count_to_palindrome(arr) == res
