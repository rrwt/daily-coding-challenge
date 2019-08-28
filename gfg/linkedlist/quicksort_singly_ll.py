"""
Quicksort on singly linkedlist
"""
from typing import Optional, Tuple


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None


def partition(head: Node, tail: Node) -> Tuple[Node, Optional[Node]]:
    prev, runner = None, head

    while runner != tail:
        if runner.data < tail.data:
            if prev:
                prev = prev.next
            else:
                prev = head
            prev.data, runner.data = runner.data, prev.data

        if runner.next:
            runner = runner.next
        else:
            break

    if not prev:
        head.data, tail.data = tail.data, head.data
        return head, head

    if prev.next:
        tail.data, prev.next.data = prev.next.data, tail.data

    return prev, prev.next


def quicksort(head: Optional[Node], tail: Optional[Node]) -> None:
    if head is not None and tail is not None and tail != head:
        prev, pivot = partition(head, tail)
        quicksort(head, prev)

        if pivot:
            quicksort(pivot.next, tail)


if __name__ == "__main__":
    head: Node = Node(3)
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

        if head.next:
            head = head.next
        else:
            break
