"""
Invert a binary tree.

For example, given the following tree:
    a
   / \
  b   c
 / \  /
d   e f

should become:
  a
 / \
 c  b
 \  / \
  f e  d
"""
from typing import Optional
from daily_problems.binary_tree_node import Node, inorder_traversal


def invert_tree(root_node: Optional[Node] = None) -> Optional[Node]:
    if root_node:
        root_node.left, root_node.right = root_node.right, root_node.left
        invert_tree(root_node.right)
        invert_tree(root_node.left)

    return root_node


if __name__ == "__main__":
    root = Node("a")
    root.left = Node("b")
    root.right = Node("c")
    root.left.left = Node("d")
    root.left.right = Node("e")
    root.right.left = Node("f")
    print("inorder traversal")
    inorder_traversal(root)
    print("inorder traversal of inverted tree")
    inorder_traversal(invert_tree(root))
