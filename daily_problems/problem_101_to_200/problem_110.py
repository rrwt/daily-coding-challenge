"""
Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5

Return [[1, 2], [1, 3, 4], [1, 3, 5]].
"""
from typing import Optional, List

from daily_problems.binary_tree_node import Node


def bin_tree_path(root_node: Optional[Node]) -> List[List[int]]:
    if not root_node:
        return [[]]

    if root_node.left is None and root_node.right is None:
        return [[root_node.data]]

    return_list = []

    if root_node.left:
        for path in bin_tree_path(root_node.left):
            return_list.append([root_node.data] + path)

    if root_node.right:
        for path in bin_tree_path(root_node.right):
            return_list.append([root_node.data] + path)

    return return_list


if __name__ == "__main__":
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.right.left = Node(4)
    tree.right.right = Node(5)
    print(bin_tree_path(tree))
