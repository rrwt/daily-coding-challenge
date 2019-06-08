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
        self.root: Optional[Node] = None

    def insert(self, data: int):
        """
        time complexity: O(h). Iterative.
        """
        if self.root:
            root = self.root
            node = Node(data)

            while root.data != data:
                if root.data > data:
                    if root.left:
                        root = root.left
                    else:
                        break
                elif root.data < data:
                    if root.right:
                        root = root.right
                    else:
                        break

            if root.data > data:
                root.left = node
            else:
                root.right = node
        else:
            self.root = Node(data)

        return self

    def search(self, data: int) -> str:
        """
        time complexity: O(h). Iterative.
        """
        root = self.root

        if root:
            while root and root.data != data:
                if root.data > data:
                    root = root.left
                elif root.data < data:
                    root = root.right

            return "Found" if root else "Not Found"
        return "Not Found"

    def min_value_node(self, node) -> int:
        if node:
            while node.left:
                node = node.left

        return node.data if node else -1

    def delete(self, root, data: int):
        """3 cases
        1. Node has no children: delete the node
        2. Node has right child: Copy inorder data into the node and delete inorder successor
        3. Node has only left child: replace node with it's left child

        Expected Time complexity: O(h)
        """
        if root:
            if data < root.data:
                root.left = self.delete(root.left, data)
            elif data > root.data:
                root.right = self.delete(root.right, data)
            elif root.right:  # data = root.data
                root.data = self.min_value_node(root.right)
                root.right = self.delete(root.right, root.data)
                return root
            else:  # data = root.data and root.right is None
                return root.left

        return root


def inorder(root: Optional[Node]):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


if __name__ == "__main__":
    bst = BST()
    bst.insert(50).insert(30).insert(20).insert(40).insert(70).insert(60).insert(80)
    inorder(bst.root)
    print()
    print(bst.search(20))
    print("Deleting 50")
    bst.delete(bst.root, 50)
    inorder(bst.root)
    print()
