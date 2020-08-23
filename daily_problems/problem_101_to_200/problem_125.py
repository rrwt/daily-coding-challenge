"""
Given the root of a binary search tree, and a target K,
return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20
    10
   /   \
 5      15
       /  \
     11    15
Return the nodes 5 and 15.
"""
from typing import Tuple, List, Optional

from daily_problems.binary_tree_node import Node


def get_sorted_values(root_node: Node) -> List[Optional[int]]:
    """
    Inorder traversal of BST results in a sorted list.
    """
    if not root_node:
        return []

    return (
        get_sorted_values(root_node.left)
        + [root_node.data]
        + get_sorted_values(root_node.right)
    )


def get_sum_nodes(root_node: Node, k: int) -> Optional[Tuple[int, int]]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    while root_node.data > k:
        root_node = root_node.left

    values = get_sorted_values(root_node)

    start_index = 0
    end_index = len(values) - 1

    while start_index < end_index:
        sum_val = values[start_index] + values[end_index]

        if sum_val == k:
            return values[start_index], values[end_index]
        elif sum_val > k:
            end_index -= 1
        else:
            start_index += 1

    return None


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(11)
    root.right.right = Node(15)

    assert get_sum_nodes(root, 20) == (5, 15)
