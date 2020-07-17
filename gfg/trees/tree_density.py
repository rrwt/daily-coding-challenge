"""
Get density of a binary tree in one traversal
"""
from typing import Optional

from gfg.trees.binary_tree_node import Node  # type: ignore


def density(root_node: Node) -> float:
    def in_order(node: Optional[Node], height: int = 1):
        nonlocal nodes
        nonlocal max_height
        if node:
            in_order(node.left, height + 1)
            max_height = max(height, max_height)
            nodes += 1
            in_order(node.right, height + 1)

    nodes: int = 0
    max_height: int = 0

    in_order(root_node)
    print("nodes:", nodes, "; max_height:", max_height)

    return nodes / max_height if max_height else 0


if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.right = Node(5)

    print(density(root))

