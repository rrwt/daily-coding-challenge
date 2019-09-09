"""
Given the roots of a tree. print out all of its
root-to-leaf paths one per line
"""
from typing import Optional

from binary_tree_node import Node  # type: ignore


def root_to_leaf_path(root: Optional[Node], stack: list = []) -> None:
    if root is not None:
        if root.left is None and root.right is None:
            print(stack + [root.data], sep="->")
            return

        root_to_leaf_path(root.left, stack + [root.data])
        root_to_leaf_path(root.right, stack + [root.data])


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root_to_leaf_path(root)
