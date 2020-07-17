"""
Given the roots of a tree. print out all of its
root-to-leaf paths one per line
"""
from typing import Optional

from gfg.trees.binary_tree_node import Node  # type: ignore


def print_root_to_leaf(node: Optional[Node] = None, stack: Optional[list] = None) -> None:
    if not node:
        return None
    if not stack:
        stack = []

    if node.left is None and node.right is None:
        print(*(stack + [node.data]), sep="->")
    else:
        print_root_to_leaf(node.left, stack + [node.data])
        print_root_to_leaf(node.right, stack + [node.data])


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print_root_to_leaf(root)
