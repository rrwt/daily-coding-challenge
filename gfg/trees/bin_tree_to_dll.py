"""
Given a Binary Tree (Bt), convert it to a Doubly Linked List(DLL).
The left and right pointers in nodes are to be used as previous and next pointers
respectively in converted DLL. The order of nodes in DLL must be same as Inorder
of the given Binary Tree.
The first node of Inorder traversal (left most node in BT) must be head node of the DLL.
"""
from typing import Optional

from binary_tree_node import Node  # type: ignore


def inorder_dll(tree: Optional[Node]) -> Optional[Node]:
    if tree:
        node = Node(tree.data)
        if tree.left:
            left = inorder_dll(tree.left)
            if left:
                while left.right:
                    left = left.right

                node.left = left
                left.right = node
        if tree.right:
            right = inorder_dll(tree.right)

            if right:
                while right.left:
                    right = right.left

                node.right = right
                right.left = node

        return node
    return None


def print_dll(dll: Node):
    while dll:
        print(dll.data)
        dll = dll.right


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)

    root = inorder_dll(root)
    while root.left:
        root = root.left

    print_dll(root)
