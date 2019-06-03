"""
Morris Traversal for preorder traversing
"""
from binary_tree_node import Node  # type: ignore


def morris_preorder(root: Node):
    print("morris preorder traversal")

    while root:
        if root.left:
            head = root.left

            while head.right and head.right != root:
                head = head.right

            if head.right:
                head.right = None
                root = root.right
            else:
                print(root.data, end=" ")
                head.right = root
                root = root.left
        else:
            print(root.data, end=" ")
            root = root.right

    print("\n", "End morris preorder traversal", sep="")


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

    morris_preorder(root)
