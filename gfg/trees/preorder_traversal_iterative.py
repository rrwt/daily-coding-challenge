"""
Iterative preorder traversal
"""
from binary_tree_node import Node  # type: ignore


def iterative_preorder(root: Node):
    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        print(node.data)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


if __name__ == "__main__":
    """
        1
     2     3
   4   5 6   7
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    iterative_preorder(root)
