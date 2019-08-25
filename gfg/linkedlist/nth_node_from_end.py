"""
Given a Linked List and a number n, write a function that returns
the value at the n’th node from the end of the Linked List.
"""
from random import randint
from typing import Optional


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Optional[Node] = None


def nth_from_end(head: Optional[Node], k: int) -> int:
    first = second = head

    while k and first is not None:
        first = first.next
        k -= 1

    while first is not None and second is not None:
        first = first.next
        second = second.next

    if second is not None:
        return second.data

    return -1


if __name__ == "__main__":
    head = Node(1)
    temp = head

    for i in range(2, 10):
        temp.next = Node(i)
        temp = temp.next

    for _ in range(5):
        k = randint(1, 9)
        print("element", k, "from end is:", nth_from_end(head, k))

    print("element", 9, "from end is:", nth_from_end(head, 9))
