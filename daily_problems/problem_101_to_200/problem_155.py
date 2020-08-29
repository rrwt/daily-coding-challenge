"""
Given a list of elements, find the majority element,
which appears more than half the time (> floor(len(lst) / 2.0)).
You can assume that such element exists.
"""
from typing import List


def majority_element(elements: List[int]) -> int:
    """
    Using Moore's Voting algorithm and assuming that there is a majority element
    Time Complexity: O(n)
    """
    maj = elements[0]
    count = 1

    for index, element in enumerate(elements[1:], start=1):
        if element == maj:
            count += 1
        else:
            count -= 1

            if count == 0:
                maj = element
                count = 1

    return maj


if __name__ == "__main__":
    assert majority_element([3, 3, 4, 2, 4, 4, 2, 4, 4]) == 4
