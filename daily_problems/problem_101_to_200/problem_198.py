"""
Given a set of distinct positive integers,
find the largest subset such that every pair of elements
in the subset (i, j) satisfies either i % j = 0 or j % i = 0.

For example,
    given the set [3, 5, 10, 20, 21], you should return [5, 10, 20].
    given [1, 3, 6, 24], return [1, 3, 6, 24].
"""
from typing import List


def largest_subset(numbers: List[int]) -> List[int]:
    numbers.sort()
    max_count = 0
    index = 0
    size = len(numbers)
    max_subset = []

    while index < size - max_count:
        subset = [numbers[index]]
        count = 1

        for j in range(index + 1, size):
            if numbers[j] % numbers[index] == 0:
                subset.append(numbers[j])
                count += 1

        if max_count < count:
            max_count = count
            max_subset = subset

        index += 1

    return max_subset if max_count > 1 else []


if __name__ == "__main__":
    assert largest_subset([3, 5, 10, 20, 21]) == [5, 10, 20]
    assert largest_subset([1, 3, 6, 24]) == [1, 3, 6, 24]
