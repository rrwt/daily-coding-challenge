"""
Given a binary tree and two values say n1 and n2,
write a program to find the least common ancestor.
"""
from typing import Optional

from binary_tree_node import Node  # type: ignore


def lowest_common_ancestor(root: Optional[Node], n1: int, n2: int) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)  # stack
    """

    def ancestor(node: Optional[Node]) -> bool:
        nonlocal return_value
        if node is None:
            return False

        if node.left is None and node.right is None:
            return node.data in (n1, n2)

        is_ancestor = node.data in (n1, n2)

        if return_value == -1:
            left = ancestor(node.left)
        if return_value == -1:
            right = ancestor(node.right)

        if return_value == -1 and (
            (left and right) or (is_ancestor and left) or (is_ancestor and right)
        ):
            return_value = node.data

        return left or right or is_ancestor

    return_value = -1
    ancestor(root)
    return return_value


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(lowest_common_ancestor(root, 1, 2))
    print(lowest_common_ancestor(root, 4, 5))
    print(lowest_common_ancestor(root, 4, 6))
    print(lowest_common_ancestor(root, 2, 4))
