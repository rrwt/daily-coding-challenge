"""
Given the sequence of keys visited by a postorder traversal of a binary search tree,
reconstruct the tree.

For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:
        5
       / \
      3   7
     / \   \
    2   4   8
"""
from typing import List, Optional

from daily_problems.binary_tree_node import Node, inorder_traversal


def find_index_of_smaller(numbers: List[int], start_index: int, last_index: int) -> int:
    for i in range(last_index - 1, start_index - 1, -1):
        if numbers[i] < numbers[last_index]:
            return i

    return start_index - 1


def find_index_of_larger(numbers: List[int], start_index: int, last_index: int) -> int:
    for i in range(last_index - 1, start_index - 1, -1):
        if numbers[i] > numbers[last_index]:
            return i

    return start_index - 1


def _construct_bst(
    postorder: List[int], start_index: int, end_index: int
) -> Optional[Node]:
    if end_index < start_index:
        return None

    root = Node(postorder[end_index])

    left_last_index = find_index_of_smaller(postorder, start_index, end_index)
    root.left = _construct_bst(postorder, start_index, left_last_index)

    root.right = _construct_bst(
        postorder,
        left_last_index + 1,
        find_index_of_larger(postorder, left_last_index + 1, end_index),
    )
    return root


def bst_from_postorder_traversal(postorder: List[int]) -> Optional[Node]:
    return _construct_bst(postorder, 0, len(postorder) - 1)


if __name__ == "__main__":
    inorder_traversal(bst_from_postorder_traversal([2, 4, 3, 8, 7, 5]))
