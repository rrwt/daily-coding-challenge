"""
Given a binary tree, check whether it is a mirror of itself without recursion.
"""
from typing import Optional
from collections import deque

from binary_tree_node import Node  # type: ignore


def is_mirror_recursive(root: Optional[Node]) -> bool:
    def verify_left_right(left: Optional[Node], right: Optional[Node]) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        return (
            left.data == right.data
            and verify_left_right(left.left, right.right)
            and verify_left_right(left.right, right.left)
        )

    if root is None:
        return True

    return verify_left_right(root.left, root.right)


def is_mirror_iterative(root: Optional[Node]) -> bool:
    if root is None:
        return True

    first_queue = deque([root.left])
    second_queue = deque([root.right])

    while first_queue and second_queue:
        node_1 = first_queue.popleft()
        node_2 = second_queue.popleft()

        if node_1 is None and node_2 is None:
            continue

        if node_1 is None or node_2 is None:
            return False

        if node_1.data != node_2.data:
            return False

        if node_1.left:
            first_queue.append(node_1.left)
            second_queue.append(node_2.right)

        if node_1.right:
            first_queue.append(node_1.right)
            second_queue.append(node_2.left)

    if first_queue or second_queue:
        return False

    return True


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(3)
    root.right.left = Node(3)
    root.right.right = Node(4)
    assert is_mirror_recursive(root) is True
    assert is_mirror_iterative(root) is True

    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.right = Node(3)
    root.right.right = Node(3)
    assert is_mirror_recursive(root) is False
    assert is_mirror_iterative(root) is False
