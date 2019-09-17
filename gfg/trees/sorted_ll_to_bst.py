"""
Given a Singly Linked List which has data members sorted in ascending order.
Construct a Balanced Binary Search Tree which has same data members as the given Linked List.
"""
from typing import Optional

from binary_tree_node import Node  # type: ignore
from tree_traversal import inorder  # type: ignore


class LLNode:
    def __init__(self, data: int):
        self.data = data
        self.next: Optional[LLNode] = None


def ll_size(head: Optional[LLNode]) -> int:
    temp = head
    count = 0

    while temp:
        temp = temp.next
        count += 1

    return count


def sorted_ll_to_bst(head: Optional[LLNode]) -> Optional[Node]:
    def construct(length: int) -> Optional[Node]:
        nonlocal head

        if head is None or length == 0:
            return None

        left = construct(length // 2)
        root = Node(head.data)
        head = head.next
        root.left = left
        root.right = construct(length - length // 2 - 1)
        return root

    return construct(ll_size(head))


if __name__ == "__main__":
    head = LLNode(1)
    head.next = LLNode(2)
    head.next.next = LLNode(3)

    inorder(sorted_ll_to_bst(head))
    print()

    head = LLNode(1)
    head.next = LLNode(2)
    head.next.next = LLNode(3)
    head.next.next.next = LLNode(4)
    head.next.next.next.next = LLNode(5)
    head.next.next.next.next.next = LLNode(6)
    head.next.next.next.next.next.next = LLNode(7)

    inorder(sorted_ll_to_bst(head))
    print()
