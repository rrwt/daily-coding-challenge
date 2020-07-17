"""
Construct and count all possible bst for keys 1 to N
"""
from typing import Optional, Sequence

from gfg.trees.binary_tree_node import Node  # type: ignore
from gfg.trees.tree_traversal import preorder  # type: ignore


def fact(n: int) -> int:
    if n <= 1:
        return 1

    return n * fact(n - 1)


def count_bst(n: int) -> int:
    return int((fact(2 * n) / fact(n)) / fact(n + 1))


def construct_bst(min_value: int = 0, max_value: int = 0) -> Sequence[Optional[Node]]:
    if min_value > max_value:
        return [None]

    root_list: list = []

    for i in range(min_value, max_value + 1):
        left_subtrees = construct_bst(min_value, i - 1)
        right_subtrees = construct_bst(i + 1, max_value)

        for left in left_subtrees:
            for r in right_subtrees:
                right = r
                root = Node(i)
                root.left = left
                root.right = right
                root_list.append(root)

    return root_list


if __name__ == "__main__":
    for index in range(1, 6):
        print("for n =", index, ", the number of possible bsts are: ", count_bst(index))
        print("preorder traversals of possible trees are:")
        list_trees = construct_bst(1, index)

        for tree in list_trees:
            preorder(tree)
            print()
