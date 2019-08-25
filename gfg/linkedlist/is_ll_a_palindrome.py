"""
Given a singly linked list of characters, write a function that returns true
if the given list is a palindrome, else false.
"""
from typing import Optional


class Node:
    def __init__(self, data: str) -> None:
        self.data = data
        self.next: Optional[Node] = None


def is_palindrome(head: Optional[Node]) -> bool:
    def verify(node: Optional[Node]) -> bool:
        nonlocal head

        if node is None:
            return True

        if node.next is None:
            return head.data == node.data

        if verify(node.next):
            head = head.next
            return node.data == head.data

        return False

    if head is None:
        return True

    temp = head
    return verify(temp)


if __name__ == "__main__":
    head = Node("R")
    head.next = Node("A")
    head.next.next = Node("D")
    head.next.next.next = Node("A")
    head.next.next.next.next = Node("R")

    assert is_palindrome(head)
