"""
To iteeratively traverse a tree in an inorder manner
"""
from binary_tree_node import Node


def inorder_iterative(root: Node):
    """
    Using temporary stack to store the current root
    while left child is being traversed
    space: O(n)
    time: O(n)
    """
    stack = []

    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
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
