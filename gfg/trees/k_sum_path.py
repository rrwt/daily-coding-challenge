"""
A binary tree and a number k are given. Print every path in the
tree with sum of the nodes in the path as k.
A path can start from any node and end at any node and must be
downward only, i.e. they need not be root node and leaf node;
and negative numbers can also be there in the tree
"""
from typing import Optional

from binary_tree_node import Node  # type: ignore


def k_sum_paths(root: Optional[Node], k: int, path: list) -> None:
    if root is None:
        return None

    path.append(root.data)
    k_sum_paths(root.left, k, path)
    k_sum_paths(root.right, k, path)

    total = 0

    for index in range(len(path) - 1, -1, -1):
        total += path[index]

        if total == k:
            print(path[index:])

    path.pop()


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(3)
    root.left.left = Node(2)
    root.left.right = Node(1)
    root.left.right.left = Node(1)
    root.right = Node(-1)
    root.right.left = Node(4)
    root.right.left.left = Node(1)
    root.right.left.right = Node(2)
    root.right.right = Node(5)
    root.right.right.right = Node(2)

    k = 5
    k_sum_paths(root, k, [])
