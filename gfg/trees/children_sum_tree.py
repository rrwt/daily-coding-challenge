"""
Given an arbitrary binary tree, convert it to a binary tree that holds
Children Sum Property. You can only increment data values in any node
(You cannot change the structure of the tree and cannot decrement the value of any node).
"""
from typing import Optional

from binary_tree_node import Node  # type: ignore
from tree_traversal import inorder  # type: ignore


def increment_children_data(root: Node, diff: int) -> None:
    if root.left is not None:
        root.left.data += diff
        increment_children_data(root.left, diff)
    elif root.right is not None:
        root.right.data += diff
        increment_children_data(root.right, diff)


def children_sum(root: Optional[Node]) -> int:
    if root is None:
        return 0

    if root.left is not None or root.right is not None:
        left_sum = children_sum(root.left)
        right_sum = children_sum(root.right)
        diff = left_sum + right_sum - root.data

        if diff > 0:
            root.data += diff
        elif diff < 0:
            increment_children_data(root, -diff)

    return root.data


if __name__ == "__main__":
    """
             50
          7       2
       3    5   1   30
    """
    root = Node(50)
    root.left = Node(7)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(1)
    root.right.right = Node(30)
    children_sum(root)
    inorder(root)
    print()
