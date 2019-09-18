"""
Given an array of size n. The problem is to check whether the given array
can represent the level order traversal of a Binary Search Tree or not.
"""
from collections import deque


def check_level_order_bst(level_order: list) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    length: int = len(level_order)
    queue = deque()

    queue.append([level_order[0], -1_000_000, 1_000_000])
    index = 1

    while index < length and queue:
        node, min_val, max_val = queue.popleft()

        if index < length and (min_val < level_order[index] < node):
            queue.append([level_order[index], min_val, node])
            index += 1
        if index < length and (node < level_order[index] < max_val):
            queue.append([level_order[index], node, max_val])
            index += 1

    if index == length:
        return True

    return False


if __name__ == "__main__":
    assert check_level_order_bst([7, 4, 12, 3, 6, 8, 1, 5, 10]) is True
    assert check_level_order_bst([11, 6, 13, 5, 12, 10]) is False
