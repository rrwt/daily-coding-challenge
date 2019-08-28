"""
Quicksort on singly linkedlist
"""
from typing import Optional, Tuple


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None


def partition(head: Node, tail: Node) -> Tuple[Node, Node]:
    prev, runner = None, head

    while runner != tail:
        if runner.data < tail.data:
            if prev:
                prev = prev.next
            else:
                prev = head
            prev.data, runner.data = runner.data, prev.data

        runner = runner.next

    if not prev:
        prev = head
        head.data, tail.data = tail.data, head.data
    else:
        tail.data, prev.next.data = prev.next.data, tail.data
    return prev, prev.next


def quicksort(head: Optional[Node], tail: Optional[Node]) -> Optional[Node]:
    if head is not None and tail != head and head.next != tail:
        pivot, prev = partition(head, tail)
        quicksort(head, prev)
        quicksort(pivot.next, tail)


if __name__ == "__main__":
    head = Node(3)
    tail = head
    tail.next = Node(2)
    tail = tail.next
    tail.next = Node(4)
    tail = tail.next
    tail.next = Node(5)
    tail = tail.next
    tail.next = Node(1)
    tail = tail.next

    quicksort(head, tail)

    print("sorted data")
    while head:
        print(head.data)
        head = head.next
