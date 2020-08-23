"""
Given k sorted singly linked lists,
write a function to merge all the lists into one sorted singly linked list.
"""
import sys
from typing import List

from daily_problems.linked_list import Node


def merge_linked_list(sorted_ll: List[Node]) -> Node:
    head = tail = None

    while any(sorted_ll):
        min_val = sys.maxsize
        next_node = 0

        for index, pointer in enumerate(sorted_ll):
            if pointer and pointer.data < min_val:
                min_val = pointer.data
                next_node = index

        if tail:
            tail.next = sorted_ll[next_node]
            tail = tail.next
        else:
            head = tail = sorted_ll[next_node]

        sorted_ll[next_node] = sorted_ll[next_node].next

    return head


if __name__ == "__main__":
    l1 = Node(0)
    l1.next = Node(3)
    l1.next.next = Node(4)
    l2 = Node(1)
    l2.next = Node(5)
    l3 = Node(2)

    node = merge_linked_list([l1, l2, l3])

    while node:
        print(node.data)
        node = node.next
