"""
Recall that a full binary tree is one in which each node is either a leaf node,
or has two children. Given a binary tree, convert it to a full one by removing
nodes with only one child.

For example, given the following tree:
         0                                              0
      /     \                                        /     \
    1         2    You should convert it to:       5        4
  /            \                                          /   \
3               4                                        6     7
 \            /   \
   5         6     7
"""
from typing import Optional

from daily_problems.binary_tree_node import Node, inorder_traversal


def binary_tree_to_full_binary_tree(root_node: Optional[Node]) -> Optional[Node]:
    if root_node is None:
        return None

    left_node = binary_tree_to_full_binary_tree(root_node.left)
    right_node = binary_tree_to_full_binary_tree(root_node.right)

    if left_node is not None and right_node is None:
        return left_node
    elif right_node is not None and left_node is None:
        return right_node

    root_node.left = left_node
    root_node.right = right_node
    return root_node


if __name__ == "__main__":
    root = Node(0)
    root.left = Node(1)
    root.left.left = Node(3)
    root.left.left.right = Node(5)
    root.right = Node(2)
    root.right.right = Node(4)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)

    print("original tree traversal")
    inorder_traversal(root)
    print("full tree traversal")
    inorder_traversal(binary_tree_to_full_binary_tree(root))
