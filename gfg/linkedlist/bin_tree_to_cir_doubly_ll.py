"""
Given a Binary Tree, convert it to a Circular Doubly Linked List (In-Place).
The left and right pointers in nodes are to be used as previous and next
pointers respectively in converted Circular Linked List.
The order of nodes in List must be same as Inorder of the given Binary Tree.
The first node of Inorder traversal must be head node of the Circular List.
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


def create_dll(
    left: Optional[Node], root_data: int, right: Optional[Node]
) -> Optional[Node]:
    node = Node(root_data)

    if not (left or right):
        node.left = node.right = node
        return node
    elif not left:
        node.right = right
        node.left = right.left
        right.left.right = node
        right.left = node
        return node
    elif not right:
        node.left = left.left
        node.right = left
        left.left.right = node
        left.left = node
        return left
    else:
        node.left = left.left
        node.right = right
        left.left.right = node
        right.left.right = left
        left.left = right.left
        right.left = node
        return left


def bin_tree_to_circular_and_doubly_linked_list(root: Optional[Node]) -> Optional[Node]:
    if root:
        left = bin_tree_to_circular_and_doubly_linked_list(root.left)
        right = bin_tree_to_circular_and_doubly_linked_list(root.right)
        return create_dll(left, root.data, right)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)
    head = bin_tree_to_circular_and_doubly_linked_list(root)
    temp = head

    while True:
        print(temp.data, end="->")
        temp = temp.right
        if temp.right == head:
            break
    if temp:
        print(temp.data)
