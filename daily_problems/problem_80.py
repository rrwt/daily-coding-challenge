"""
Given the root of a binary tree, return a deepest node.
For example, in the following tree, return d.
    a
   / \
  b   c
 /
d
"""
from typing import Optional

from daily_problems.binary_tree_node import Node


def get_deepest_node(root_node: Optional[Node] = None) -> str:
    def get_deepest(node: Optional[Node] = None, level: int = 0) -> None:
        nonlocal max_level, deepest_node

        if not node:
            return None
        if node.left:
            get_deepest(node.left, level+1)
        if node.right:
            get_deepest(node.right, level+1)
        if level > max_level:
            max_level = level
            deepest_node = node.data

    max_level = 0
    deepest_node = root_node.data if root_node else ""
    get_deepest(root_node)
    return deepest_node


if __name__ == "__main__":
    root = Node("a")
    root.left = Node("b")
    root.left.left = Node("d")
    root.right = Node("c")
    assert get_deepest_node(root) == "d"
