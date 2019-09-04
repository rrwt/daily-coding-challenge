from typing import Union, Optional


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def morris_inorder(root: Node) -> None:
    while root is not None:
        if root.left:
            left = root.left

            while left.right and left.right != root:
                left = left.right

            if left.right == root:
                left.right = None
                print(root.data)
                root = root.right
            else:
                left.right = root
                root = root.left
        else:
            print(root.data)
            root = root.right


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    morris_inorder(root)
