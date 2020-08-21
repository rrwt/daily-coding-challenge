"""
Given a sorted list of integers,
square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""
from typing import List


def merge_sorted_lists(first: List[int], second: List[int]) -> List[int]:
    i, j, l1, l2 = 0, 0, len(first), len(second)
    merged_list = []

    while i < l1 and j < l2:
        if first[i] <= second[j]:
            merged_list.append(first[i])
            i += 1
        else:
            merged_list.append(second[j])
            j += 1

    if i < l1:
        merged_list.extend(first[i:])
    elif j < l2:
        merged_list.extend(second[j:])

    return merged_list


def square_and_sort(numbers: List[int]) -> List[int]:
    """
    O(n) & O(n)
    """
    numbers = list(map(lambda x: x*x, numbers))
    length = len(numbers)
    index_of_0 = -1

    for i in range(length):
        if numbers[i] == 0:
            index_of_0 = i
            break

    first_list = list(reversed(numbers[:index_of_0]))
    second_list = numbers[index_of_0:]

    return merge_sorted_lists(first_list, second_list)


if __name__ == "__main__":
    assert square_and_sort([-9, -2, 0, 2, 3]) == [0, 4, 4, 9, 81]
