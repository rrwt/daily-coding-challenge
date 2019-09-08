"""
Given a binary tree, you need to check whether sum of all covered elements
is equal to sum of all uncovered elements or not. In a binary tree, a node
is called Uncovered if it appears either on left boundary or right boundary.
Rest of the nodes are called covered.
"""
from typing import Optional

from binary_tree_node import Node  # type: ignore


def get_tree_sum(root) -> int:
    if not root:
        return 0

    return root.data + get_tree_sum(root.left) + get_tree_sum(root.right)


def get_uncovered_sum(root) -> int:
    if not root:
        return 0

    temp = root.left
    total = root.data

    while temp:
        total += temp.data
        if temp.left:
            temp = temp.left
        else:
            temp = temp.right

    temp = root.right

    while temp:
        total += temp.data
        if temp.right:
            temp = temp.right
        else:
            temp = temp.left

    return total


def check_sum(root: Optional[Node]) -> bool:
    if root is None or (root.left is None and root.right is None):
        return True

    temp = root
    tree_sum = get_tree_sum(temp)

    if tree_sum & 1:
        return False

    temp = root
    uncovered_sum = get_uncovered_sum(temp)

    return uncovered_sum == tree_sum / 2


if __name__ == "__main__":
    root = Node(8)
    root.left = Node(3)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    root.right = Node(10)
    root.right.right = Node(14)
    root.right.right.left = Node(13)

    assert check_sum(root) == False
