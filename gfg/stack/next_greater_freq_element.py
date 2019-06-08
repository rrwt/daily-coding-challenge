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
    result: list = [None] * len(elements)
    freq: dict = defaultdict(int)
    stack: list = []
    top = -1

    for element in elements:  # get freq per element
        freq[element] += 1

    stack.append(0)
    top += 1

    for i, element in enumerate(elements[1:]):
        if freq[elements[stack[top]]] < freq[element]:
            while freq[elements[stack[top]]] < freq[element]:
                result[stack.pop()] = element
                top -= 1

        stack.append(i + 1)
        top += 1

    while stack:
        result[stack.pop()] = -1

    return result


if __name__ == "__main__":
    print(next_greater_freq_element([1, 1, 2, 3, 4, 2, 1]))
