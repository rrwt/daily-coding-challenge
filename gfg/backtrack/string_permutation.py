"""
Write all permutations of a string
"""


def permute(string_arr: list, left: int, right: int) -> None:
    """
    Time Complexity: O(n!*n)
    """

    if left == right:
        print(string_arr)
    else:
        for index in range(left, right + 1):
            string_arr[index], string_arr[left] = string_arr[left], string_arr[index]
            permute(string_arr, left + 1, right)
            string_arr[index], string_arr[left] = string_arr[left], string_arr[index]


if __name__ == "__main__":
    permute(["A", "B", "C"], 0, 2)
