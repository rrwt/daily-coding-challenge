"""
Given the head of a singly linked list, reverse it in-place.
"""
from typing import Optional

from daily_problems.linked_list import Node


def reverse_ll(head_node: Node) -> Node:
    prev_node: Optional[Node] = None

    while head_node:
        next_node = head_node.next
        head_node.next = prev_node
        prev_node = head_node
        head_node = next_node

    return prev_node


if __name__ == "__main__":
    head: Node = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    new_head: Node = reverse_ll(head)

    while new_head:
        print(new_head.data)
        new_head = new_head.next
