"""
binary tree to dll
"""
from typing import Optional


class Node:
    """
    Works as a node for both tree and DLL
    """

    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def inorder_conversion(root: Optional[Node]) -> Optional[Node]:
    if root:
        left = inorder_conversion(root.left)
        head = Node(root.data)
        right = inorder_conversion(root.right)

        if left:
            while left.right:
                left = left.right

            left.right = head
            head.left = left
        if right:
            while right.left:
                right = right.left

            right.left = head
            head.right = right

        return head
    return root


def inorder_conversion2(root: Optional[Node]) -> Optional[Node]:
    def inorder(root: Optional[Node]) -> None:
        nonlocal head, prev
        if root:
            inorder(root.left)

            if prev is None:
                head = root
            else:
                prev.right = root
                root.left = prev

            prev = root
            inorder(root.right)

    head: Optional[Node] = None
    prev: Optional[Node] = None
    inorder(root)
    return head


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)
    head = inorder_conversion2(root)

    while head and head.right:
        print(head.data, end="->")
        head = head.right
    if head:
        print(head.data)
