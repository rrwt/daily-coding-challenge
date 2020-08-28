"""
Given a pivot x, and a list lst, partition the list into three parts.
    The first part contains all elements in lst that are less than x
    The second part contains all elements in lst that are equal to x
    The third part contains all elements in lst that are larger than x
Ordering within a part can be arbitrary.
"""
from typing import List


def three_way_q_sort(numbers: List[int], pivot: int) -> List[int]:
    i, j, size = -1, 0, len(numbers)
    k = size

    while j < k:
        if numbers[j] < pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j += 1
        elif numbers[j] > pivot:
            k -= 1
            numbers[j], numbers[k] = numbers[k], numbers[j]
        else:
            j += 1

    return numbers


if __name__ == "__main__":
    print(three_way_q_sort([9, 12, 3, 5, 14, 10, 10], 10))
    print(three_way_q_sort([9, 12, 3, 5, 14, 10, 10], 9))
    print(three_way_q_sort([9, 12, 3, 5, 14, 10, 10], 12))
