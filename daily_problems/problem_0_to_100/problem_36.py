"""
Given the root to a binary search tree, find the second largest node in the tree.
"""
from typing import Optional, Union, Tuple

from daily_problems.binary_tree_node import Node  # type: ignore


def get_second_largest(root_node: Optional[Node]) -> Optional[Union[int, str]]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    If root has a right child, then largest/second largest node cannot be part of the left subtree
    If root doesn't have a right child, then the second largest node will be the largest element of
    left subtree
    """
    if not root_node:
        return None

    while root_node.right and (root_node.right.left or root_node.right.right):
        root_node = root_node.right

    if root_node.right:
        return root_node.data

    root_node = root_node.left

    while root_node and root_node.right:
        root_node = root_node.right

    return root_node.data if root_node else None


def get_second_largest_alt(root_node: Node) -> Optional[int]:
    def get_largest_child(node, parent_node) -> Tuple[Node, Node]:
        while node and node.right:
            parent_node = node
            node = node.right
        return node, parent_node

    if root_node is None:
        return None

    if root_node.left is None and root_node.right is None:
        return None

    if root_node.right is None:
        largest = root_node.data
        parent = None
    else:
        parent = root_node
        largest, parent = get_largest_child(root_node.right, parent)

    if largest.left:
        return get_largest_child(largest.left, parent)[0].data
    else:  # parent node
        return parent.data


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(8)

    assert get_second_largest(root) == 7
    assert get_second_largest_alt(root) == 7
