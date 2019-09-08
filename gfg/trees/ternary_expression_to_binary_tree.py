"""
Given a string that contains ternary expressions. The expressions may be nested,
task is convert the given ternary expression to a binary Tree.
"""
from typing import Optional

from binary_tree_node import Node  # type: ignore
from tree_traversal import inorder  # type: ignore


def get_left_ending(expression, start, end) -> int:
    for index in range(start, end + 1):
        pass


def create_tree(expression: str) -> Optional[Node]:
    def construct():
        nonlocal index, length

        if index >= length:
            return None

        root = Node(expression[index])
        index += 1

        if index < length - 1:
            if expression[index] == "?":
                index += 1
                root.left = construct()
                index += 1
                root.right = construct()

        return root

    index = 0
    length = len(expression)
    return construct()


if __name__ == "__main__":
    inorder(create_tree("a?b:c"))
    print()
    inorder(create_tree("a?b?c:d:e"))
    print()
    inorder(create_tree("a?b?c:d:e?f:g"))
    print()
