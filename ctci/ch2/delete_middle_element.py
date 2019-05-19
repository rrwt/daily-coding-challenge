"""
Implement an algorithm to delete a node in the middle (i.e., any node but the
first and last node, not necessarily the exact middle) of a singly linked list,
given only access to that node.
"""
import sys


class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Node = None


class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head

    def push(self, data: int):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
            h = self.head

            while h.next:
                h = h.next

            h.next = node

        return self

    def delete_middle(self, middle: Node) -> int:
        head: Node = self.head

        while head and head.next != middle:
            head = head.next

        data: int = None

        if head:
            data = head.next.data
            head.next = head.next.next

        return data


if __name__ == "__main__":
    ll = LinkedList(Node(1))
    ll.push(2)
    ll.push(3)

    print("expected", 2, sep=" ")
    print("result:", ll.delete_middle(ll.head.next), sep=" ")

    h = ll.head

    while h:
        print(h.data)
        h = h.next
