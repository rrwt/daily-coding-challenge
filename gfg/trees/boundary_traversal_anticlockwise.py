"""
Traverse the boundaries of a binary tree in anticlockwise fashion
"""
from gfg.trees.binary_tree_node import Node  # type: ignore


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
    root_node = Node(1)
    root_node.left = Node(2)
    root_node.right = Node(3)
    root_node.left.left = Node(4)
    root_node.left.right = Node(5)
    root_node.right.left = Node(6)
    root_node.right.right = Node(7)
    boundary_traverse(root_node)
