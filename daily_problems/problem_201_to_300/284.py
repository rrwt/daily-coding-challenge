"""
Two nodes in a binary tree can be called cousins if they
are on the same level of the tree but have different parents.
For example, in the following diagram 4 and 6 are cousins.
    1
   / \
  2   3
 / \   \
4   5   6
Given a binary tree and a particular node, find all cousins of that node.
"""
from collections import deque
from typing import List

from daily_problems.binary_tree_node import Node


def cousin_nodes(root_node: Node, data: int) -> List[int]:
    res = []

    if root_node.data == data:
        return res

    queue = deque()
    queue.append((root_node, 0))
    target_level = -1

    while queue:
        cur_node, level = queue.popleft()

        if level == target_level and cur_node.data != data:
            res.append(cur_node.data)
        elif level > target_level > -1:
            break

        if cur_node.left:
            if cur_node.left.data == data:
                target_level = level + 1
            queue.append((cur_node.left, level + 1))

        if cur_node.right:
            if cur_node.right.data == data:
                target_level = level + 1
            queue.append((cur_node.right, level + 1))

    return res


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    assert cousin_nodes(root, 4) == [5, 6]
