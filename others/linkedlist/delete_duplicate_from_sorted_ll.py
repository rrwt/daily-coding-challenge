"""
You're given the pointer to the head node of a sorted linked list,
where the data in the nodes is in ascending order. Delete as few nodes
as possible so that the list does not contain any value more than once.
The given head pointer may be null indicating that the list is empty.
"""
from typing import Optional


class LL:
    def __init__(self, head: Optional[int]):
        self.head = LL.Node(head) if head else None

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def append(self, data: int):
        node = LL.Node(data)

        head = self.head

        if head:
            while head.next:
                head = head.next
            head.next = node
        else:
            self.head = node

        return self

    def delete(self, data: int):
        node = None

        if self.head.data == data:
            node = self.head
            self.head = self.head.next
        else:
            head = self.head

            while head.next and head.next.data != data:
                head = head.next

            if head.next:
                node = head.next
                head.next, node.next = node.next, None

        return node


def delete_duplicates(ll: LL) -> LL:
    head = ll.head

    while head:
        while head.next and head.next.data == head.data:
            head.next = head.next.next

        head = head.next

    return ll


if __name__ == "__main__":
    ll = LL(1)
    ll.append(1).append(2).append(2).append(3).append(4)
    ll = delete_duplicates(ll)

    head = ll.head

    while head:
        print(head.data)
        head = head.next
