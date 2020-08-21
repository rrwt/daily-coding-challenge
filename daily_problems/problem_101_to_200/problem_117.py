"""
Given a binary tree, return the level of the tree with minimum sum.
"""
import sys
from collections import deque, defaultdict

from daily_problems.binary_tree_node import Node


def level_with_min_sum(root_node: Node) -> int:
    q = deque()  # to traverse nodes in Level Order Fashion
    d = defaultdict(list)  # to store level sum

    # insert node and level
    q.append((root_node, 0))

    while q:
        node, level = q.popleft()
        d[level].append(node.data)

        if node.left:
            q.append((node.left, level + 1))
        if node.right:
            q.append((node.right, level + 1))

    min_sum = sys.maxsize
    min_sum_level = 0

    for level, values in d.items():
        cur_sum = sum(values)
        if cur_sum < min_sum:
            min_sum = cur_sum
            min_sum_level = level

    return min_sum_level


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    assert level_with_min_sum(root) == 1
