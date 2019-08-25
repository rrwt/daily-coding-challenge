"""
Given a Linked List of integers, write a function to modify the linked list
such that all even numbers appear before all the odd numbers in the modified
linked list. Also, keep the order of even and odd numbers same.
"""
from typing import Optional, Tuple


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Optional[Node] = None


def last_element(head: Optional[Node]) -> Tuple[Optional[Node], int]:
    temp = head
    elem_count = 1

    while temp and temp.next:
        temp = temp.next
        elem_count += 1

    return (temp, elem_count) if temp else (None, 0)


def segregate(head: Optional[Node]) -> Optional[Node]:
    tail, elem_count = last_element(head)
    temp = head
    prev = None

    for _ in range(elem_count):
        if temp.data & 1:
            if prev:
                prev.next = temp.next
                tail.next = temp
                tail = tail.next
                temp = prev.next
            elif tail:
                tail.next = temp
                tail = tail.next
                head = temp.next
                temp = head
            tail.next = None
        else:
            prev = temp
            temp = temp.next

    return head


def print_ll(head: Optional[Node]) -> None:
    temp = head

    while temp and temp.next:
        print(temp.data, end="->")
        temp = temp.next

    if temp:
        print(temp.data)


if __name__ == "__main__":
    head = Node(17)
    temp = head

    for elem in [15, 8, 12, 10, 5, 4, 1, 7, 6, 9]:
        temp.next = Node(elem)
        temp = temp.next

    print("original list")
    print_ll(head)
    print("final list")
    new_head = segregate(head)
    print_ll(new_head)
