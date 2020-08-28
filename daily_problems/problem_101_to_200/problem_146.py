"""
Given a binary tree where all nodes are either 0 or 1,
prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:
       0
      / \
     1   0
        / \
       1   0
      / \
     0   0

should be pruned to:
       0
      / \
     1   0
        /
       1
We do not remove the tree at the root or its left child because it still has a 1 as a descendant.
"""
from typing import Optional

from daily_problems.binary_tree_node import Node
from gfg.trees.tree_traversal import inorder


def prune(node: Optional[Node]) -> Optional[Node]:
    if not node:
        return None

    node.left = prune(node.left)
    node.right = prune(node.right)

    if node.data == 1 or node.left or node.right:
        return node

    return None


if __name__ == "__main__":
    tree = Node(0)
    tree.left = Node(1)
    tree.right = Node(0)
    tree.right.left = Node(1)
    tree.right.left.left = Node(0)
    tree.right.left.right = Node(0)

    tree = prune(tree)
    inorder(tree)
