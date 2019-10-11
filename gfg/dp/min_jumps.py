"""
Given an array of integers where each element represents the max number of steps
that can be made forward from that element. Write a function to return the minimum
number of jumps to reach the end of the array (starting from the first element).
If an element is 0, then cannot move through that element.
"""


def min_jumps(arr: list) -> int:
    """
    Time Complexity: O(n*n)
    """

    length: int = len(arr)

    if length == 0 or arr[0] == 0:
        return -1

    if length == 1:
        return 0

    jumps: list = [length + 1] * length
    jumps[0] = 0

    for index, element in enumerate(arr[:-1]):
        for j in range(index + 1, min(element + index + 1, length)):
            jumps[j] = min(jumps[index] + 1, jumps[j])

    return jumps[length - 1]


if __name__ == "__main__":
    assert min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]) == 3
    assert min_jumps([1, 3, 6, 1, 0, 9]) == 3
