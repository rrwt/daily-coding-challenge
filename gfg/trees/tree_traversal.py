from collections import deque
from typing import Union, Optional


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def inorder(root: Optional[Node]) -> None:
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root: Optional[Node]) -> None:
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root: Optional[Node]) -> None:
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


def level_order(root: Optional[Node]) -> None:
    if root is not None:
        queue: deque = deque()
        queue.append(root)

        while queue:
            element = queue.popleft()
            print(element.data, end=" ")

            if element.left is not None:
                queue.append(element.left)
            if element.right is not None:
                queue.append(element.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    print("Inorder traversal")
    inorder(root)
    print()
    print("preorder traversal")
    preorder(root)
    print()
    print("postorder traversal")
    postorder(root)
    print()
    print("level order traversal")
    level_order(root)
    print()
