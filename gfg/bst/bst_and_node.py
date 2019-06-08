"""
Binary Search Tree and Tree node
"""
from typing import Optional


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BST:
    """BST
    Data less than that of node goes in the left subtree and data more than that
    of node goes in the right subtree recursively. No two nodes can have same data.
    h: height of tree
    n: total number of nodes
    in worst cast the height of binary search tree becomes n
    """

    def __init__(self):
        self.head: Optional[Node] = None

    def insert(self, data: int):
        """
        time complexity: O(h). Iterative.
        """
        if self.head:
            head = self.head
            node = Node(data)

            while head.data != data:
                if head.data > data:
                    if head.left:
                        head = head.left
                    else:
                        break
                elif head.data < data:
                    if head.right:
                        head = head.right
                    else:
                        break

            if head.data > data:
                head.left = node
            else:
                head.right = node
        else:
            self.head = Node(data)

        return self

    def search(self, data: int) -> str:
        """
        time complexity: O(h). Iterative.
        """
        head = self.head

        if head:
            while head and head.data != data:
                if head.data > data:
                    head = head.left
                elif head.data < data:
                    head = head.right

            return "Found" if head else "Not Found"
        return "Not Found"


def inorder(root: Optional[Node]):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


if __name__ == "__main__":
    bst = BST()
    bst.insert(50).insert(30).insert(20).insert(40).insert(70).insert(60).insert(80)
    inorder(bst.head)
    print()
    print(bst.search(20))
