"""
Given an integer N, construct all possible binary search trees with N nodes.
"""
from typing import List, Optional

from daily_problems.binary_tree_node import Node, level_order_traversal


def construct_bst(start: int, end: int) -> List[Optional[Node]]:
    if start > end:
        return [None]

    return_list = []

    for index in range(start, end + 1):
        left_subtrees = construct_bst(start, index - 1)
        right_subtrees = construct_bst(index + 1, end)

        for left in left_subtrees:
            for right in right_subtrees:
                root = Node(index)
                root.left = left
                root.right = right
                return_list.append(root)

    return return_list


if __name__ == "__main__":
    for n in range(1, 6):
        print(f"bst of size {n}")

        for bst in construct_bst(0, n - 1):
            level_order_traversal(bst)
            print()
