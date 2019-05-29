"""
To iteeratively traverse a tree in an inorder manner
"""
from typing import Optional
from binary_tree_node import Node  # type: ignore


def inorder_iterative(root: Optional[Node]):
    """
    Using temporary stack to store the current root
    while left child is being traversed
    space: O(n)
    time: O(n)
    """
    stack: list = []

    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()

        if root:
            print(root.data, end=" ")
            root = root.right
    print()


def inorder_iterative_with_constant_space(root: Node):
    """
    Morris Traversal
    Instead of using a stack to traverse back we can use the right node of the
    rightmost child of left child of ccurrent node to traverse back to root.
    Time Complexity: O(n)
    """
    while root:
        if root.left:
            head = root.left

            while head.right and head.right != root:
                head = head.right

            if head.right == root:
                head.right = None
                print(root.data, end=" ")
                root = root.right
            else:
                head.right = root
                root = root.left
        else:
            print(root.data, end=" ")
            root = root.right

    print()


if __name__ == "__main__":
    """
    Constructed binary tree is 
              1 
            /   \
          2      3 
        /  \
      4     5 
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    inorder_iterative(root)
    inorder_iterative_with_constant_space(root)
