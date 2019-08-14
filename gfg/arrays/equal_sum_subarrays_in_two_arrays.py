"""
Given two binary arrays arr1[] and arr2[] of same size n.
Find length of the longest common span (i, j) where j >= i
such that arr1[i] + arr1[i+1] + …. + arr1[j] = arr2[i] + arr2[i+1] + …. + arr2[j].
"""


def subarray(a: list, b: list) -> int:
    """
    Time Complexity: O(n)
    """
    l: int = len(a)
    hash_table: dict = {a[0] - b[0]: 0}
    length: int = 0

    for i in range(1, l):
        a[i] += a[i - 1]
        b[i] += b[i - 1]
        diff = a[i] - b[i]

        if diff == 0:
            length = i + 1
        elif diff in hash_table:
            length = max(length, i - hash_table[diff])
        else:
            hash_table[diff] = i

    return length


if __name__ == "__main__":
    arr_list: list = [[[0, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 1]]]

    for (a, b) in arr_list:
        print(subarray(a, b))
