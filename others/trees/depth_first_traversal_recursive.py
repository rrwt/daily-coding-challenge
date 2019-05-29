"""
Depth first traversal includes 3 traversing methods:
1. Inorder
2. Preorder
3. Postorder
"""
from typing import Optional

from binary_tree_node import Node


def inorder(root: Optional[Node]) -> None:
    """
    In inorder traversal we recursively traverse in following manner:
        1. We traverse the left subtree
        2. We visit the current node
        3. We traverse the right subtree
    """
    if not root:
        return None

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def preorder(root: Optional[Node]) -> None:
    """
    In preorder traversal we recursively traverse in the following manner:
        1. Visit the current node
        2. Traverse the left subtree
        3. Traverse the right subtree
    """
    if not root:
        return None

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


def postorder(root: Optional[Node]) -> None:
    """
    In postorder traversal we recursively traverse in the following manner:
        1. Traverse the left subtree
        2. Traverse the right subtree
        3. Visit the current node
    """
    if not root:
        return None

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


if __name__ == "__main__":
    """
            1
    2               3
4       5
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("inorder traversal:")
    inorder(root)
    print("\npreorder traversal:")
    preorder(root)
    print("\npostorder traversal:")
    postorder(root)
    print()
