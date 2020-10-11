"""
A girl is walking along an apple orchard with a bag in each hand.
She likes to pick apples from each tree as she goes along,
but is meticulous about not putting different kinds of apples in the same bag.
Given an input describing the types of apples she will pass on her path,
in order, determine the length of the longest portion of her path that
consists of just two types of apple trees.

For example, given the input [2, 1, 2, 3, 3, 1, 3, 5],
the longest portion will involve types 1 and 3, with a length of four.
"""
from collections import defaultdict
from typing import List


def max_apples(apples: List[int]) -> int:
    type_count = defaultdict(int)
    max_size = 0
    start = 0
    apple_types = set()

    for index, apple_type in enumerate(apples):
        apple_types.add(apple_type)
        type_count[apple_type] += 1

        while len(apple_types) > 2:
            type_count[apples[start]] -= 1

            if type_count[apples[start]] == 0:
                apple_types.remove(apples[start])

            start += 1

        max_size = max(max_size, index - start + 1)

    return max_size


if __name__ == "__main__":
    assert max_apples([2, 1, 2, 3, 3, 1, 3, 5])
