"""
Given an array, for each element find the value of nearest element to the right
which is having frequency greater than as that of current element. If there does
not exist an answer for a position, then make the value ‘-1’.
"""
from collections import defaultdict


def next_greater_freq_element(elements: list) -> list:
    """
    time complexity: O(n)
    using a dictionary to count frequency.
    using a stack to keep track of next greater
    """
    result: list = [-1] * len(elements)
    freq: dict = defaultdict(int)
    stack: list = []

    for element in elements:
        freq[element] += 1

    for i, element in enumerate(elements):
        while stack and freq[elements[stack[-1]]] < freq[element]:
            result[stack[-1]] = element
            stack.pop()

        stack.append(i)

    return result


if __name__ == "__main__":
    print(next_greater_freq_element([1, 1, 2, 3, 4, 2, 1]))
    print(next_greater_freq_element([1, 1, 1, 2, 2, 2, 2, 11, 3, 3]))
