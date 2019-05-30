"""
Given a Binary Tree where each node has following structure, write a function to
populate next pointer for all nodes. The next pointer for every node should be
set to point to inorder successor.
"""
from typing import Optional


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Optional[Node] = None
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def fill_inorder_successor(root: Optional[Node]):
    """
    traverse in reverse in-order and populate the next pointer
    """

    def reverse_inorder(node: Optional[Node]):
        nonlocal next

        if node:
            reverse_inorder(node.right)
            node.next = next
            next = node
            reverse_inorder(node.left)

    next: Optional[Node] = None
    reverse_inorder(root)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    fill_inorder_successor(root)

    while root.left:
        root = root.left

    while root.next:
        print(root.data, end=" ")
        root = root.next
    print(root.data)
