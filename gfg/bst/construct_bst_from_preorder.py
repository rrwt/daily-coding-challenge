"""
Given preorder traversal of a binary search tree, construct the BST.

For example, if the given traversal is {10, 5, 1, 7, 40, 50},
then the output should be root of following tree.
     10
   /   \
  5     40
 / \     \
1   7    50
"""
from typing import Optional

from bst_and_node import Node, inorder  # type: ignore


def find_greater(elements: list, data: int) -> int:
    for i, elem in enumerate(elements):
        if elem > data:
            return i + 1

    return -1


def get_bst(preorder: list) -> Node:
    """
    time complexity: O(n*n)
    space complexity: O(n)
    """

    def construct_tree(elements: list) -> Optional[Node]:
        if elements:
            node = Node(elements[0])

            if len(elements) > 1:
                greater = find_greater(elements[1:], node.data)

                if greater != -1:
                    node.left = construct_tree(elements[1:greater])
                    node.right = construct_tree(elements[greater:])
            return node

        return None

    return construct_tree(preorder)


if __name__ == "__main__":
    print(inorder(get_bst([10, 5, 1, 7, 40, 50])))
