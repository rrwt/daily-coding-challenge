"""
Given a Binary Tree, write a function to check whether the given Binary Tree
is a prefect Binary Tree or not. A Binary tree is Perfect Binary Tree in which
all internal nodes have two children and all leaves are at same level.

A perfect binary tree is full and complete
"""
from typing import Optional

from gfg.trees.binary_tree_node import Node  # type: ignore


def is_perfect(root: Optional[Node]) -> bool:
    def is_full_and_complete(root: Optional[Node], node_level: int) -> bool:
        nonlocal level

        if root is None:
            return True

        if root.left is None and root.right is None:
            return node_level == level

        if root.left is None or root.right is None:
            return False

        return is_full_and_complete(root.left, node_level + 1) and is_full_and_complete(
            root.right, node_level + 1
        )

    temp = root
    level = 0

    while temp and temp.left:
        temp = temp.left
        level += 1

    return is_full_and_complete(root, 0)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)
    assert is_perfect(root) == True
