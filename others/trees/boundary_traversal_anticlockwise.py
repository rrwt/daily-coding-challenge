"""
Traverse the boundaries of a binary tree in anticlockwise fashion
"""
from binary_tree_node import Node  # type: ignore


def left_boundary(root: Node):
    """
    Do not print leaves
    """
    if root:
        if root.left:
            print(root.data)
            left_boundary(root.left)
        elif root.right:
            print(root.data)
            left_boundary(root.right)


def right_boundary(root: Node):
    if root:
        if root.right:
            right_boundary(root.right)
            print(root.data)
        elif root.left:
            right_boundary(root.left)
            print(root.data)


def leaves(root: Node):
    """
    Same as inorder traversal
    """
    if root:
        leaves(root.left)

        if not (root.left or root.right):
            print(root.data)

        leaves(root.right)


def boundary_traverse(root: Node):
    print(root.data)
    left_boundary(root.left)
    leaves(root)
    right_boundary(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    boundary_traverse(root)
