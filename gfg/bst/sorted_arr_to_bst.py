"""
Given a sorted array. Write a function that creates a
Balanced Binary Search Tree using array elements.
"""
from typing import Optional

from gfg.bst.bst_and_node import Node, inorder  # type: ignore


def sorted_arr_to_bst(arr: list) -> Node:
    """
    time complexity: O(n)
    space complexity: O(n)  # array and stack
    """

    def construct_bst(elements) -> Optional[Node]:
        length = len(elements)

        if length <= 0:
            return None

        if length == 1:
            return Node(elements[0])

        root_position = int(length / 2)
        root = Node(elements[root_position])
        root.left = construct_bst(elements[:root_position])
        root.right = construct_bst(elements[root_position + 1 :])
        return root

    return construct_bst(arr)


if __name__ == "__main__":
    from random import randint

    for _ in range(5):
        inorder(sorted_arr_to_bst(list(range(randint(2, 20)))))
        print()
