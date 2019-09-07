"""
Construct a binary tree from a string consisting of parenthesis and integers.
The whole input represents a binary tree. It contains an integer followed by
zero, one or two pairs of parenthesis. The integer represents the root’s value
and a pair of parenthesis contains a child binary tree with the same structure.
Always start to construct the left child node of the parent first if it exists.
"""
from typing import Optional

from binary_tree_node import Node  # type: ignore
from tree_traversal import inorder  # type: ignore


def get_subtree_string(string, start: int, end: int) -> int:
    stack = []

    for index in range(start, end + 1):
        if string[index] == ")":
            stack.pop()
        elif string[index] == "(":
            stack.append(string[index])

        if not stack:
            return index


def construct_bin_tree(string: str) -> Optional[Node]:
    length = len(string)

    if length == 0:
        return None

    root = Node(string[0])

    if length > 1:
        left_end_index = get_subtree_string(string, 1, length - 1)
        root.left = construct_bin_tree(string[2:left_end_index])

        if left_end_index < length - 2:
            root.right = construct_bin_tree(string[left_end_index + 2 : length - 1])

    return root


if __name__ == "__main__":
    inorder(construct_bin_tree(""))
    print()
    inorder(construct_bin_tree("1(2)(3)"))
    print()
    inorder(construct_bin_tree("4(2(3)(1))(6(5))"))
    print()
