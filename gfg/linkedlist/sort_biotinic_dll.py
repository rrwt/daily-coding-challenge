"""
Sort the given biotonic doubly linked list. A biotonic doubly linked list
is a doubly linked list which is first increasing and then decreasing.
A strictly increasing or a strictly decreasing list is also a biotonic doubly linked list.
"""
from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


def reverse(head: Optional[Node]) -> Optional[Node]:
    prev, temp = None, head

    while temp:
        next = temp.next

        if prev:
            prev.prev = temp
            temp.next = prev

        prev = temp
        temp = next

    if prev and head:
        head.next = None
        prev.prev = None
    return prev


def merge(first: Optional[Node], second: Optional[Node]) -> Optional[Node]:

    if first is None:
        return second
    if second is None:
        return first

    if first.data <= second.data:
        head = first
        first = first.next
    else:
        head = second
        second = second.next

    runner = head

    while first and second:
        if first.data <= second.data:
            runner.next = first
            first.prev = runner
            runner = first
            first = first.next
        else:
            runner.next = second
            second.prev = runner
            runner = second
            second = second.next

    if first:
        runner.next = first
        first.prev = runner
    elif second:
        runner.next = second
        second.prev = runner

    return head


def sort_dll(head: Optional[Node]) -> Optional[Node]:
    """
    3 cases:
        1. Already sorted. Do nothing
        2. reverse sorted. Reverse the entire dll
        3. There is a peak, reverse the second half and merge.
    """
    if head is None:
        return None

    runner = head

    while runner.next and runner.data < runner.next.data:
        runner = runner.next

    if runner.next:
        if runner == head:
            return reverse(head)
        elif runner.prev:
            runner.prev.next = None
            runner.prev = None
            return merge(head, reverse(runner))

    return head


def print_ll(head: Optional[Node]) -> None:
    while head and head.next:
        print(head.data, end="->")
        head = head.next

    if head is not None:
        print(head.data)


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next
    print_ll(sort_dll(head))

    head = Node(4)
    head.next = Node(3)
    head.next.prev = head
    head.next.next = Node(2)
    head.next.next.prev = head.next
    head.next.next.next = Node(1)
    head.next.next.next.prev = head.next.next
    print_ll(sort_dll(head))

    head1 = Node(1)
    head1.next = Node(3)
    head1.next.next = Node(5)
    head1.next.next.next = Node(7)
    head1.next.prev = head1
    head1.next.next.prev = head1.next
    head1.next.next.next.prev = head1.next.next

    head2 = Node(6)
    head2.next = Node(4)
    head2.next.next = Node(2)
    head2.next.next.next = Node(0)
    head2.next.prev = head2
    head2.next.next.prev = head2.next
    head2.next.next.next.prev = head2.next.next
    head1.next.next.next.next = head2
    head2.prev = head1.next.next.next
    print_ll(sort_dll(head1))
