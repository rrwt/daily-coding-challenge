"""
Given the head of a singly linked list, reverse it in-place.
"""
from typing import Optional

from linked_list import Node


def reverse_ll(head: Node) -> Node:
    prev: Optional[Node] = None

    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev


if __name__ == "__main__":
    head: Node = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    new_head: Node = reverse_ll(head)

    while new_head:
        print(new_head.data)
        new_head = new_head.next
