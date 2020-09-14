"""
Typically, an implementation of in-order traversal of a binary tree
has O(h) space complexity, where h is the height of the tree.
Write a program to compute the in-order traversal of a binary tree using O(1) space.
"""
from daily_problems.binary_tree_node import Node


def inorder(node: Node) -> None:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    while node:
        if node.left:
            runner = node.left

            while runner.right and runner.right != node:
                runner = runner.right

            if runner.right == node:
                runner.right = None
                print(node.data)
                node = node.right
            else:
                runner.right = node
                node = node.left
        else:
            print(node.data)
            node = node.right


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(7)
    inorder(root)
